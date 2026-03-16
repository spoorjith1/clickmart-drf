from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email" #using this we can login with email
    REQUIRED_FIELDS = ["username"] #this is needed because when we create superuser it needs username
    
    def __str__(self):
        return self.email