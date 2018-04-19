# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from .models import User, UserManager
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
# Create your views here.
def dashboard(request):
	return render(request, "posts/dashboard.html")

def post_html(request):
	posts = Post.objects.filter(user_posts=User.objects.get(id=request.session['id'])).order_by('-created_at')
	return render(request, "posts/posts.html", {'posts': posts})
def create_post(request):
	print request.POST
	print request.session['id']
	user_posts = User.objects.get(id=request.session['id'])
	print user_posts
	post = Post.objects.create(
		title=request.POST['title'],
		content=request.POST['content'],
		user_posts=user_posts
		)
	posts = Post.objects.filter(user_posts=user_posts).order_by('-created_at')
	return render(request, "posts/posts.html", {'posts': posts})

def delete(request):
	user_posts = User.objects.get(id=request.session['id'])
	print request.POST['number']
	Post.objects.get(id=request.POST['number']).delete()
	posts = Post.objects.filter(user_posts=user_posts).order_by('-created_at')
	return render(request,"posts/posts.html", {'posts': posts})

def edit(request):
	print request.POST
	print request.POST['number']
	edit = Post.objects.get(id=request.POST['number'])
	edit.title = request.POST['title']
	edit.content = request.POST['content']
	edit.save()
	user_posts = User.objects.get(id=request.session['id'])
	posts = Post.objects.filter(user_posts=user_posts).order_by('-created_at')
	return JsonResponse(model_to_dict(edit))
# def update(request, number):
# 	pass
	# print number
	# posts = Post.objects.get(id=number)
	# return render(request, "posts/edit.html", {'posts': posts})