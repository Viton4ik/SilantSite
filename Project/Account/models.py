from django.contrib.auth.models import User
from django.db import models

from App.models import Role

class User_Auth(models.Model):
    user_auth = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    role_auth = models.ForeignKey(Role, on_delete=models.DO_NOTHING) 
   
