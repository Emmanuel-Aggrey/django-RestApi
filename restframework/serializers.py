from rest_framework import  serializers

from  .models import Person
from  django.contrib.auth.models import  User
class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model =Person
        fields = [
        'name',
        'age',
        'contact',
        'url',
        ]

