from django import forms
from django.contrib.auth.models import User
from main.models import Blog

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

#class SignInForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput())
#    class Meta():
#        model = User
#        fields = ('username', 'password')

class BlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = Blog
        fields = ('bid', 'title', 'username', 'content')
