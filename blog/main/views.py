# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from . import forms

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, "index.html", {
        'post_list': post_list,
        });

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        if form.is_valid():
            # Do something.
            print("Form Validation Success. Prints in console.")
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['email'])
            print('Text'+form.cleaned_data['text'])
    return render(request,'form_page.html',{'form':form})
