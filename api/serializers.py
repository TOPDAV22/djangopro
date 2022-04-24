
from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token 

from django.core.exceptions import ValidationError
from uuid import uuid4
from django.db.models import Q
from rest_framework.validators import UniqueValidator


class ArticleSerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Article 
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=20, min_length=6)
    password = serializers.CharField(max_length=100, write_only=True)
    username = serializers.CharField(max_length=50,min_length=6)

    class Meta:
        model = User
        fields = ['first_name','email','username', 'password']

    def validate (self, args):
        email = args.get('email', None)
        username = args.get ('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already used')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already used')})
        return super().validate(args)

      
    def create(self, validated_data):
       
        return User.objects.create_User(**validated_data)

