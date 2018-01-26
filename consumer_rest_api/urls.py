from django.conf.urls import url
from django.conf.urls import include
from . import receiver

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

urlpatterns = [
    url(r'^data/$', views.MessagesApiView.as_view())
]
receiver.start()