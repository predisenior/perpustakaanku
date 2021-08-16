from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    alamat = models.TextField(null=True, blank=True)
    photo = models.ImageField(blank=True,null=True, upload_to='profile/')
    
