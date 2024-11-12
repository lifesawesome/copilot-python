import json
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import datetime


@api_view(['GET'])
def get_current_time(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse({'time': current_time}, status=status.HTTP_200_OK)

# Create a new function GET hello?key=World that returns a JSON response with the key value in the query parameter.
@api_view(['GET'])
def get_hello(request):
    key = request.GET.get('key')
    if not key:
        raise NotFound('Query parameter "key" not found')
    return JsonResponse({'key': key}, status=status.HTTP_200_OK)

#Create a new GET view that read the ./data/vms.json file and return the JSON content
@api_view(['GET'])
def get_azure_vms(request):
    with open('./data/vms.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
# CREATE A NEW VIEW THAT RETURNS THE CONTENT OF home.html
@api_view(['GET'])
def about(request):
    with open('./data/vms.json', 'r', encoding='utf-8') as f:
        vms = json.load(f)
    return render(request, 'home.html', {'vms': vms})
