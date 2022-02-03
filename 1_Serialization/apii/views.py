from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
#model object - single student data

def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print (json_data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data )
    # used content_type to tell which data is going in response i.e json data


# Query Set = All Student Data
def student_list(request):
    stu = Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu, many=True)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print (json_data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe=False)
    # used content_type to tell which data is going in response i.e json data
