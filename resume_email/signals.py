from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ResumeEmail
from .tasks import resume_email_created

@receiver(post_save, sender=ResumeEmail)
def send_resume_email(sender, instance, created, **kwargs):
    if created:
        # launch asynchronous task
        resume_email_created.delay(instance.id)


@receiver(post_delete, sender=ResumeEmail)
def send_resume_email(sender, instance, **kwargs):
    instance.resume_file.delete(False)