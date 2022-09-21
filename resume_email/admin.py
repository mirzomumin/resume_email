from django.contrib import admin

from .models import ResumeEmail
# Register your models here.


@admin.register(ResumeEmail)
class AdminResumeEmail(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'phone', 'email', 'resume_file')