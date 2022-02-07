from enroll.models import StudentInfo
from enroll.api.serializers import StudentInfoSerializer
from rest_framework import viewsets
from rest_framework.authentication import  SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StudentInfoViewSet(viewsets.ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
