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
	search = {
		"category": request.POST['categoryId'],
		"lat": request.POST['Lat'],
		"lng": request.POST['Lng']
	}
	print search
	return redirect('/activity')