from django.test import TestCase, Client
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

class userLogInAndOutTest(TestCase):

    def test_login_and_logout(self):
        self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
        User.objects.create_user(**self.credentials)

        self.client = Client()
        response = self.client.post(reverse('main:user_login'), **self.credentials)
        self.assertEquals(response.status_code, 200)
        self.client.login(username='testuser', password="secret")
        response = self.client.post(reverse('main:user_logout'))
        self.assertRedirects(response, reverse('index'))

class blog_Test(TestCase):

    def test_blog_form(self):
        self.client = Client()
        response = self.client.post(reverse('main:blog_form'))
        self.assertTemplateUsed(response, 'main/blog_form.html')

    def test_blog_proc(self):
        post_data =  { 
                'title': 'TitleV1',
                'username': 'TestUser',
                'content': 'TestContent'
        }
        response = self.client.post(reverse('main:blog_proc'), post_data)
        blog_count  = Blog.objects.filter(title='TitleV1').count()
        self.assertEquals(blog_count, 1)
        blog  = Blog.objects.get(title='TitleV1')
        self.assertEquals(blog.bid,1)

    def tes_list_page(self):
        self.client = Client()
        response = self.client.post(reverse('main:list_page'))
        self.assertRedirects(response, reverse('index'))
    
    def test_update_proc(self):
        post_data_before_update = {
                'title': 'TitleV1',
                'username': 'TestUser',
                'content': 'TestContent'
        }
        response = self.client.post(reverse('main:blog_proc'), post_data_before_update)
        blog = Blog.objects.get(title='TitleV1')
        post_updated_data = {
                'bid': blog.bid,
                'title': blog.title,
                'username': blog.username,
                'content': 'TestContent2'
        }
        self.client = Client()
        response = self.client.post(reverse('main:update_proc'), post_updated_data)
        updated_blog = Blog.objects.get(bid=blog.bid)
        self.assertEquals(updated_blog.content, 'TestContent2')

    def test_delete_blog(self):
        post_data_before_update = {
                'title': 'TitleV1',
                'username': 'TestUser',
                'content': 'TestContent'
        }
        response = self.client.post(reverse('main:blog_proc'), post_data_before_update)
        blog_count = Blog.objects.filter(title='TitleV1').count()
        self.assertEquals(blog_count,1)

        blog = Blog.objects.get(title='TitleV1')
        post_delete_data = {
                'bid': blog.bid,
                'title': blog.title,
                'username': blog.username,
                'content': blog.content
        }

        self.client = Client()
        session = self.client.session
        session['username'] = blog.username
        session.save()
        response = self.client.get(reverse('main:delete_blog'), post_delete_data)
        self.assertRedirects(response, reverse('index'))
        blog_count = Blog.objects.filter(title='TitleV1').count()
        self.assertEquals(blog_count,0)
        del session['username']

    def test_update_blog_form_success(self):
        post_data_before_update = {
                'title': 'TitleV1',
                'username': 'TestUser',
                'content': 'TestContent'
        }
        response = self.client.post(reverse('main:blog_proc'), post_data_before_update)
        blog_count = Blog.objects.filter(title='TitleV1').count()
        self.assertEquals(blog_count,1)

        blog = Blog.objects.get(title='TitleV1')
        post_update_blog_form_data = {
                'bid': blog.bid,
                'title': blog.title,
                'username': blog.username,
                'content': blog.content
        }

        self.client = Client()
        session = self.client.session
        session['username'] = blog.username
        session.save()

        response = self.client.get(reverse('main:update_blog_form'), post_update_blog_form_data)
        self.assertTemplateUsed(response, 'main/update.html')

    def test_update_blog_form_failure(self):
        post_data_before_update = {
                'title': 'TitleV1',
                'username': 'TestUser',
                'content': 'TestContent'
        }
        response = self.client.post(reverse('main:blog_proc'), post_data_before_update)
        blog_count = Blog.objects.filter(title='TitleV1').count()
        self.assertEquals(blog_count,1)

        blog = Blog.objects.get(title='TitleV1')
        post_update_blog_form_data = {
                'bid': blog.bid,
                'title': blog.title,
                'username': blog.username,
                'content': blog.content
        }

        self.client = Client()
        session = self.client.session
        session['username'] = blog.username+"1"
        session.save()

        response = self.client.get(reverse('main:update_blog_form'), post_update_blog_form_data)
        self.assertRedirects(response, reverse('index'))
