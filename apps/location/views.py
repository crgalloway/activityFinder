# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..activity.models import category

def index(request):
	context = {
		'categories': category.objects.all()
	}
	return render(request, 'location/index.html', context)

def search(request):
	print '*'*40
	print request.POST['categoryId']
	print request.POST['Lat']
	print request.POST['Lng']
	print '*'*40