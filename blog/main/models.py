# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
