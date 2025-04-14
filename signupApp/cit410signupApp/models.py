from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User
class RegisterCourse(models.Model):
   studentID=models.IntegerField(null=False, default=000000)
   firstName=models.CharField(max_length=250, null=False, default='')
   lastName=models.CharField(max_length=250, null=False, default='')   
   courseCode="cit410"
   term="Winter A, 2024"
   date=models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.username
