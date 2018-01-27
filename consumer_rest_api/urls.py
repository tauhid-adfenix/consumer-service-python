from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views
import threading

router = DefaultRouter()

urlpatterns = [
    url(r'^data/$', views.MessagesApiView.as_view())
]