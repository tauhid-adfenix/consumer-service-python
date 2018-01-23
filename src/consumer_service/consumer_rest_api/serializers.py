from rest_framework import serializers

from . import models

class ConsumerServiceMsgSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ConsumerServiceMessages
        fields = ('uuid', 'message')
        
