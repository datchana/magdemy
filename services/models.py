from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class bookForm(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(('email address'), unique=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=False)
    message = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class registerForm(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(('email address'), unique=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=False)
    cource = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


