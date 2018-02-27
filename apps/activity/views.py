# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def activityview(request):
	context = {
		'categories': category.objects.all()
	}
	return render(request, 'activity/index.html', context)

def register(request):
	response = activity.objects.activityValidator(request.POST)
	if response['status']:
		return redirect('/activity')
	else:
		for error in response['errors']:
			messages.error(request, error)
		return redirect('/activity')