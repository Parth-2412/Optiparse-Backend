from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse as Response, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, JSONParser
from . import serializers
from rest_framework.decorators import parser_classes
from . import models

# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response('Hello')

@csrf_exempt
@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload(request):

    serializer = serializers.UploadSerializer(data={ 'file': request.FILES.get('file')})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({ 'file' : serializer.data['file'][1:]}, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['POST'])
@parser_classes([JSONParser])
def detect(request):
    file_name = request.data.get('file_name')
    if file_name == None or type(file_name) != str:
        return JsonResponse({ 'file_name' : ["This field may not be null"]}, status = 400)
    print(file_name)
    uploads = models.Upload.objects.filter(file=file_name)
    if len(uploads) == 0 :
        return JsonResponse({ 'file_name' : ["No such file"]}, status = 404)
    return JsonResponse({ }, status = 201)