from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .serializers import ResumeEmailSerializer

# Create your views here.

@api_view(['POST'])
@parser_classes((MultiPartParser,))
@permission_classes([AllowAny])
def send_resume(request):
	serializer = ResumeEmailSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({'success': 'Your resume has been accepted!'},
			status=HTTP_200_OK)
	return Response({'error': 'Your data has not been sent! Please, try again!'},
		status=HTTP_400_BAD_REQUEST)