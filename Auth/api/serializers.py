from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email' ,'password','password2']

    def validate(self, data):
        password=data.get('password')
        password2=data.pop('password2')
        if password!=password2:
            raise serializers.ValidationError('password and confirm password has not matched')
        return data
    
class UserLoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username','password']