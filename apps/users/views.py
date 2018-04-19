# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request, 'users/index.html')

def register(request):
	if request.method == "POST":
		errors = User.objects.reg_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
				return redirect('/')
		else:
			user = User.objects.new_user(request.POST)
			print user.id
			request.session['id'] = user.id
			messages.success(request, " You are registered.")
			return redirect('/posts')
	return redirect('/')

def login(request):
	if request.method == "POST":
		errors = User.objects.login_validator(request.POST)
		if type(errors) == dict:
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
				return redirect('/')
		else:
			user = User.objects.login_validator(request.POST)
			print user.id
			request.session['id'] = user.id
			messages.success(request, "You are logged in.")
			return redirect('/posts')
	return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')