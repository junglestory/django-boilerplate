from django.urls import path
from .views import *

urlpatterns = [
    path("hello/", hello),
    path("news/", news),
    path("news/<str:journal_id>/", news_list),
]