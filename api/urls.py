from django.urls import path

from . import views

urlpatterns = [
	path('send-resume-email/', views.send_resume, name='send_resume_email'),
]