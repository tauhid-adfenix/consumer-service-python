from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from django.http import HttpResponse


from . import models
from . import serializers

# Create your views here.

class MessagesApiView(APIView):
    """Messages API View."""
    serializer_class = serializers.ConsumerServiceMsgSerializer

    def get(self, request, format=None):
        """Returns a list of Consumer Service Messages."""
        queryset = models.ConsumerServiceMessages.objects.all()
        response = self.serializer_class(queryset, many=True)
        return Response(response.data)
