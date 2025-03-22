from rest_framework import serializers
from .models import JobApplication
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication  # Connects to the Job model
        fields = '__all__'  # Includes all model fields in the API

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','password']
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

