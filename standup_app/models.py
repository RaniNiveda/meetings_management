# Create your models here.
#author raniniveda
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserProfile(AbstractUser):
    mobile_number = models.CharField(blank=True, max_length=10,default="")
    address = JSONField(default=dict)
    location = JSONField(default=dict)
    state = models.CharField(blank=True,max_length=20,default="")
    city = models.CharField(blank=True,max_length=20,default="")

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super(EmployeeManager,self).get_queryset().filter(name='darika')

class Employee(models.Model):
	empid = models.CharField(max_length=10)
	name = models.CharField(max_length=30)

	#objects = models.Manager()
	emp_objects = EmployeeManager()

class Salary(models.Model):
	employee = models.ForeignKey(Employee,related_name="salary",on_delete=models.CASCADE)
	department = models.CharField(max_length=30)
	designation = models.CharField(max_length=30)
	salary = models.CharField(max_length=10)


class Project(models.Model):
	employee = models.OneToOneField(Employee,related_name="project",on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	domain=models.CharField(max_length=30)

