from django.test import TestCase
from main.models import Blog
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
import django


class BlogModelTest(TestCase):

    def setUp(self):
        self.blog = Blog()
        self.blog.title = 'This is title'
        self.blog.content = 'This is content'
        self.blog.save()

    def test_creating_new_blog(self):
        all_blog_in_database = Blog.objects.all()
        self.assertEquals(len(all_blog_in_database), 1)
        only_blog_in_database = all_blog_in_database[0]
        self.assertEquals(only_blog_in_database, self.blog)

        self.assertEquals(only_blog_in_database.title, 'This is title')
        self.assertEquals(only_blog_in_database.content, 'This is content')

    def test_blog_str(self):
        self.assertEquals(str(self.blog), 'This is title')
