# from celery import task
from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings

from .models import ResumeEmail

@shared_task
def resume_email_created(resume_email_id):
	resume_email = ResumeEmail.objects.get(id=resume_email_id)
	message = f'First Name: {resume_email.first_name}\n \n\
				Last Name: {resume_email.last_name}\n \n\
				Phone: {resume_email.phone}\n \n\
				Email: {resume_email.email}\n \n\
				Text: {resume_email.text}'
	subject = f'Resume №{resume_email.id}',
	attachment = resume_email.resume_file
	email = EmailMessage(
		subject=subject,
		body=message,
		from_email=settings.EMAIL_HOST_USER,
		to=('mirzomumin@list.ru',),
	)
	email.attach(attachment.name, attachment.read())
	response = email.send()
	return response