from django import forms
from django.contrib.auth.models import User
from main.models import UserInfo, Blog

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('profile_pic',)

class PostForm(forms.Form):
    title = forms.CharField()
    #username = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = Blog
        fields = ('title', 'username', 'content')
