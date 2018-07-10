from main.models import Blog
from main.forms import BlogForm, SignUpForm
from django.test import TestCase


class SignUpFormTest(TestCase):

    def setUp(self):
        self.username = 'TestName'
        self.email = 'email@mail.com'
        self.password = '1234'
        self.myForm = SignUpForm({
            'username': self.username,
            'email': self.email,
            'password': self.password})

    def test_SignUpFormIsValid(self):
        self.assertTrue(self.myForm.is_valid())


class BlogFormTest(TestCase):

    def setUp(self):
        self.title = 'TestTitle'
        self.content = 'TestContent'
        self.username = 'TestName'
        self.myForm = BlogForm({
            'title': self.title,
            'content': self.content,
            'username': self.username})

    def test_BlogFormIsValid(self):
        self.assertTrue(self.myForm.is_valid())
