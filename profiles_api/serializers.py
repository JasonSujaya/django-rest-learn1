from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name file for testing our api"""
    name = serializers.CharField(max_length=10)
