
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
    # only user who have staff  permission = true can access using IsAdminUser


        # we can globaly define this basic authetication so we do not need to mention
        #them in every single class explicitly, by mentioning them in settings.py.

        # in IsAuthenticated we can login being a normal user, admin and superuser as well.
        # person register hona chaiye chahe koi sa bhi user ho, phr api ko access kr  skta h.


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]

    # aese AllowAny likhne se global ko override kia ja skta h
