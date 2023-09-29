from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import ModUserManager
# Create your models here.
class ModUser(AbstractBaseUser,PermissionsMixin):
    '''user modelador'''
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150,unique= True)
    first_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(auto_now_add=True)
    about =  models.TextField(max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = ModUserManager()
    #campo identificador

    USERNAME_FIELD ='email'

    #campos requeridos para crear el superuser

    REQUIRED_FIELDS=['user_name','first_name']

    def __str__(self):
        return f"{self.user_name} {self.email}"