from django.urls import path
from .views import *

urlpatterns = [
    path("hello/", hello),
    path("news/", news),
    path("news/create/", news_create),
    path("news/update/", news_update),
    path("news/<str:journal_id>", news_list),
    path("news/<int:seq>", news_delete),
]