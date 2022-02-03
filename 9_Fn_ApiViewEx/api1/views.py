from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello_world(request):
#     return Response({'msg': 'hello world'})
#
#
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data) # request.data is parsed data
#         return Response({'msg': 'This is POST request'})


@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'This is GET response'})

    if request.method == 'POST':
        print(request.data) # request.data is parsed data
        return Response({'msg': 'This is POST request', 'data': request.data})
