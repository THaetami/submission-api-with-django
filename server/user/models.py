from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225, unique=True, validators=[validate_email])
    password = models.CharField(max_length=225)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'user'
        
    def __str__(self):
        return self.email
    
