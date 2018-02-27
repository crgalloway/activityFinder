# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class activityManager(models.Manager):
	def activityValidator(self,postData):
		response = {
			'status': True
		}
		errors = []
		if len(postData['desc']) == 0:
			errors.append("Fill out description so people know what you are doing")
		if len(postData['newCategory']) == 0:
			categoryInput = category.objects.get(id=postData['categoryId'])
		else:
			existing = category.objects.filter(name=postData['newCategory'])
			if len(existing) > 0:
				response['status'] = False
				errors.append("This category exists already") 
			else:
				categoryInput = category.objects.create(name=postData['newCategory'])
		if len(errors) == 0:
			response['activity'] = activity.objects.create(category=categoryInput,desc=postData['desc'],lat=postData['actLat'],lng=postData['actLng'])
		response['errors'] = errors
		return response		

class category(models.Model):
	name = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class activity(models.Model):
	category = models.ForeignKey(category, related_name="activities")
	desc = models.CharField(max_length = 255)
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	lng = models.DecimalField(max_digits=9, decimal_places=6)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = activityManager()