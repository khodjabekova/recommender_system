from django.db import models
from django.contrib import auth
from rest_framework import serializers
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username
