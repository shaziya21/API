from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # ek argument lgana h kisi bhi field me , use explicitly lgana pdega.
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','roll']
        extra_kwargs = {'name':{'read_only':True}}
