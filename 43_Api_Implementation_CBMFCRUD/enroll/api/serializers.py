from enroll.models import StudentInfo
from rest_framework import serializers

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ['id','name','email','password']
