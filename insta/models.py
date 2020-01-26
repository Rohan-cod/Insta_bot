from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Account(models.Model):
	user_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=50, default='xyz@gmail.com')


