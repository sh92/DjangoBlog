from django import forms
from main.models import Blog
from django.urls import reverse
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta():
        model = User
        fields = ['username', 'email', 'password']

# TODO
# class LoginForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['username', 'password']


class BlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = Blog
        fields = ('bid', 'title', 'username', 'content')

    def get_absolute_url(self):
        return reverse('main:blog_proc')
