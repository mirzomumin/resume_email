from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

# Create your models here.

class ResumeEmail(models.Model):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	phone = PhoneNumberField()
	email = models.EmailField()
	text = models.TextField(null=True, blank=True)
	resume_file = models.FileField(upload_to='resumes/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'First Name: {self.first_name}.\
		Last Name: {self.last_name}.'