from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db.models.fields import DateField, IntegerField
from .managers import UserManager
from django.utils import timezone
import datetime

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
  email       = models.EmailField(max_length=250, unique=True,
                help_text='Email should be in prooper formate',)
  PROFILE_CHOICES = (
        ('teacher', 'teacher'),
        ('student', 'student'),
        ('Admin', 'admin'),
     )
  profile = models.CharField(max_length=20, choices=PROFILE_CHOICES)              
  is_active   = models.BooleanField(default=True,
                help_text='Designates whether this user should be treated as active. '
                          'Unselect this instead of deleting accounts.')
  is_staff    = models.BooleanField(default=False,
                help_text='Designates whether the user can log into this admin site.')

  objects = UserManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'


class Teacher(models.Model):
  user    = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='teacher_detail')
  name    = models.CharField(max_length=100)
  phone   = models.IntegerField()


class Student(models.Model):
  user    = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='student_detail')
  name    = models.CharField(max_length=100)
  phone   = models.IntegerField()
  