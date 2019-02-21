# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class State(models.Model):
	state_name=models.CharField(max_length=250)
	Places=models.CharField(max_length=250)
	Religion=models.CharField(max_length=100)
	Places_pic_link=models.CharField(max_length=1000)

	def __str__(self):
		return self.state_name + '-'+ self.Places

class Capital(models.Model):
	state=models.ForeignKey(State, on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	capital_name=models.CharField(max_length=250)