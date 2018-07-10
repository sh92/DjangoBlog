from main.models import Blog
from main.forms import BlogForm
from main.forms import SignUpForm
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
