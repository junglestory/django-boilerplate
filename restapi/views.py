from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response("Hello World!")