from email import message
from unicodedata import name
from django.db import models

# Create your models here.

# class mysite(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField('User Email')

#     def __str__(self):
#         return self.first_name +' '+ self.first_name


class booking(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    address = models.CharField('Address', max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    email_address = models.EmailField('Email Address', blank=True, unique=True)
    message = models.TextField(max_length=500, null=True)

 