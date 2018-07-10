from main.forms import SignUpForm
from .models import Blog
from . import forms
from execeptions.FormException import UserFormException

from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt

# TODO pages


def index(request):
    post_list = Blog.objects.all()
    return render(request, 'main/index.html', {
        'post_list': post_list,
        })


def update_blog_form(request):
    username = request.GET['username']
    post_list = Blog.objects.all()
    if request.session['username'] != username:
        return render(request, 'main/index.html', {
            'post_list': post_list, })
    bid = request.GET['bid']
    bobject = Blog.objects.filter(bid=bid)
    return render(request, 'main/update.html', {
        'bobject': bobject,
        })


def update_proc(request):
    bid = request.POST['bid']
    title = request.POST['title']
    username = request.POST['username']
    content = request.POST['content']
    current_page = 1  # request.POST['current_page']
    Blog.objects.filter(bid=bid).update(
        title=title, username=username, content=content)
    url = '/list_page?cur_page=' + str(current_page)
    return HttpResponseRedirect(url)


def delete_blog(request):
    bid = request.GET['bid']
    username = request.GET['username']
    if request.session['username'] == username:
        b = Blog.objects.filter(bid=bid)
        for x in b:
            x.delete()
    return redirect('index')


@csrf_exempt
def blog_proc(request):
    blog = Blog(
        title=request.POST['title'],
        username=request.session['username'],
        content=request.POST['content'],
        )
    cur_page = 1
    blog.save()
    url = '/list_page?cur_page='+cur_page
    return HttpResponseRedirect(url)


def list_page(request):
    request.GET['cur_page']
    Blog.objects.all().count()
    return redirect('index')


def blog_form(request):
    form = forms.BlogForm()
    if request.method == 'POST':
        if form.is_valid():
            print('Form Validation Success')
            print(form.cleaned_data['title'])
            print(form.cleaned_data['content'])
    return render(request, 'main/blog_form.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        request.session['username'] = username

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            return HttpResponse('Your account is not active.')

        print('Someone tried to login and faild.')
        return HttpResponse('Invalid login')
    return render(request, 'main/login.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
            raise UserFormException()
    else:
        user_form = SignUpForm()

    return render(request, 'main/registration.html',
                  {'user_form': user_form,
                   'registered': registered})
