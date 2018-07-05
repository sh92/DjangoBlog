from main.forms import UserForm, UserInfoForm
from .models import Blog 
from . import forms

from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt

rowsPerPage = 2 

def index(request):
    post_list = Blog.objects.all()
    return render(request, "main/index.html", {
        'post_list': post_list,
        })

@csrf_exempt
def blog_proc(request):
    blog = Blog(
            title=request.POST['title'],
            username=request.session['username'],
            content=request.POST['content'],
            )
    blog.save()
    url = '/list_page?cur_page=1'
    return HttpResponseRedirect(url)

def list_page(request):
    cur_page = request.GET['cur_page']
    total_cnt = Blog.objects.all().count()
    print('cur_page=', cur_page)
    post_list = Blog.objects.all()
    return render(request, "main/index.html", {
        'post_list': post_list,
        })

def blog_form(request):
    form = forms.PostForm()
    if request.method == 'POST':
        if form.is_valid():
            print("Form Validation Success")
            print(form.cleaned_data['title'])
            print(form.cleaned_data['content'])
    return render(request, 'main/blog_form.html', {'form':form})

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

        print("Someone tried to login and faild.")
        return HttpResponse("Invalid login")
    return render(request, 'main/login.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserInfoForm()

    return render(request, 'main/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})
