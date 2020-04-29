from rest_framework import serializers

from .models import Person
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'age',
            'contact',
            'relationship',
        ]
