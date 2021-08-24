from Relation_test.settings import USE_I18N
from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
  #Creates, saves and returns a User.
  def create_user(self, email,  password=None,is_active=True,is_staff=False, is_superuser=False):
    if not email:
      raise ValueError("User Must have an email")
    if not password:
      raise ValueError("User Must have an password")
    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.profile = 'admin'
    user.is_active  = is_active 
    user.is_staff  = is_staff 
    user.is_superuser = is_superuser
    user.save(using=self._db) #save data to database
    return user

  def create_staffuser(self, email, password=None):
    user = self.create_user(email, password=password, is_active=True, is_staff=True)
    return user 

  def create_superuser(self, email, password=None):
    user = self.create_user(email, password=password, is_active=True, is_staff=True, is_superuser=True)
    return user 

 