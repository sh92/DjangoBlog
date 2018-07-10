from django.test import TestCase
from main.models import Blog
from main.forms import SignUpForm
from main.views import register
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render


class HomeViewTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/index.html')
        post_list = Blog.objects.all()
        post_list_context = response.context['post_list']
        self.assertQuerysetEqual(post_list, post_list_context)


class registerViewTest(TestCase):

    def test_register_valid(self):

        post_data = {
            'username': 'TestName',
            'email': 'email@mail.com',
            'password': 'TestPassword'
        }

        response = self.client.post(reverse('main:register'), post_data)
        self.assertEqual(response.status_code, 200)
        test_user = User.objects.get(username='TestName')
        self.assertEqual(test_user.username, 'TestName')
        self.assertEqual(test_user.email, 'email@mail.com')
