from django.db import models
#from django.contrib import User
from django.contrib.auth.models import User
# Create your models here.
class menu(models.Model):
	ID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	price = models.IntegerField()

	def __str__(self):
		return self.name

class custumer(models.Model):
	ID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	lat_long = models.CharField(max_length=30)
	address = models.TextField()
	email = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class deliveryMan(models.Model):
	ID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	lat_long = models.CharField(max_length=30)
	
	