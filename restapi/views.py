from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import News
from .serializers import NewsSerializer
import logging

logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response("Hello World!")


@api_view(['GET', 'POST'])
def news(request):
    if request.method == 'GET':
        datas = News.objects.all()
        serializer = NewsSerializer(datas, many=True)

        return Response(serializer.data, content_type=u"application/json; charset=utf-8")
    elif request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        # print(request.POST['journal_id'])

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def news_list(request, journal_id):
    datas = News.objects.filter(journal_id=journal_id)
    serializer = NewsSerializer(datas, many=True)
    
    return Response(serializer.data, content_type=u"application/json; charset=utf-8")


@api_view(['POST'])
def news_create(request):
    serializer = NewsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def news_update(request):
    params = request.data
    data = News.objects.get(seq=params['seq'])
    serializer = NewsSerializer(instance=data, data=params)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def news_delete(request, seq):
    data = News.objects.get(seq=seq)
    data.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)   