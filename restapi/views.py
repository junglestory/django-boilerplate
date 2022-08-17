from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import News
from .serializers import NewsSerializer
import logging

logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response("Hello World!")


@api_view(['GET'])
def news(request):
    datas = News.objects.all()
    serializer = NewsSerializer(datas, many=True)

    return Response(serializer.data, content_type=u"application/json; charset=utf-8")    