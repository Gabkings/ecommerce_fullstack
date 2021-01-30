from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, default="Anonymous")
    email = models.EmailField(max_length=150, unique=True)
    username = None

    USERNAME_FIELD = "email"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    REQUIRED_FIELDS = []
    gender = models.CharField(max_length=10, blank=True, null=True)
    session_token = models.CharField(max_length=10, default=0)
    
