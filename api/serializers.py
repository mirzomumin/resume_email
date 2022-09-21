from rest_framework import serializers

from resume_email.models import ResumeEmail


class ResumeEmailSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeEmail
		fields = ('first_name', 'last_name', 'phone', 'email', 'text', 'resume_file')