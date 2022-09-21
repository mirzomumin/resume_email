from django.apps import AppConfig


class ResumeEmailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resume_email'

    def ready(self):
        import resume_email.signals