# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from models import *
from ..users.models import User, UserManager
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	user_posts = models.ForeignKey(User, related_name="posts")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	