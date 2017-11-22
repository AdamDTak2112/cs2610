# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    content = models.TextField()
    post_date = models.DateField('Date posted')
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,)
    commenter_nickname = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    content = models.TextField()
    post_date = models.DateTimeField('Date posted')