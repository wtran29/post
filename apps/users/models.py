# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from models import *
import bcrypt
import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[A-Za-z]\w+$')
# Create your models here.
class UserManager(models.Manager):
	def reg_validator(self, postData):
		errors = {}
		if len(postData['first_name'])< 2:
			errors['first_name'] = "Invalid first name. Min 2 characters."
		elif not re.match(NAME_REGEX, postData['first_name']):
			errors['first_name'] = "Invalid entry. Must only contain letters."
		if len(postData['last_name'])< 2:
			errors['last_name'] = "Invalid last name. Min 2 characters."
		elif not re.match(NAME_REGEX, postData['last_name']):
			errors['last_name'] = "Invalid entry. Must only contain letters."

		if len(postData['email'])< 1:
			errors['email'] = "Must enter an email."
		elif self.filter(email=postData['email']).exists():
			errors['email'] = "Email already in use."
		elif not re.match(EMAIL_REGEX, postData['email']):
			errors['email'] = "Invalid email. Please try again."

		if len(postData['password'])< 8:
			errors['password'] = "Password must be at least 8 characters."
		elif postData['password']!= postData['confirm']:
			errors['password'] = "Password confirmation did not match."
		return errors

	def new_user(self, postData):
		user = User.objects.create(
			first_name=postData['first_name'],
			last_name=postData['last_name'],
			email=postData['email'],
			password=bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt(5)),
		)

		return user

	def login_validator(self, postData):
		errors = {}
		try:
			user = User.objects.get(email=postData['email'])
			if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
				errors['login_error']="Invalid email/password."
		except:
			errors['login_error'] = "Invalid login."
		if errors:
			return errors
		return user

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()


