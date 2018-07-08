from django.test import TestCase
from main.models import UserInfo, Blog
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.db import models
import os

class UserInfoModelTest(TestCase):

    user = User()
    image_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_name = 'test_image.jpg'
    image_path = image_dir+"/tests/"+image_name

    newPhoto = SimpleUploadedFile(name=image_name, content=open(image_path, 'rb').read(), content_type='image/jpeg')


    def create_UserInfo(self, profile_pic=newPhoto):
        return UserInfo.objects.create(user=self.user, profile_pic=profile_pic)

    def test_valid_UserInfo(self):
        u = self.create_UserInfo()
        self.assertTrue(isinstance(u, UserInfo))
        self.assertEquals(u.__str__(), u.user.username)

class BlogModelTest(TestCase):
    pass
