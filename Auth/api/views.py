from rest_framework.response import Response
from rest_framework import generics, status, filters, mixins
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer,UserLoginSerializer
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistraion(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid(raise_exception=True):
            print(f'serializer data is {serializer.data}')
            user = User.objects.create_user(username=serializer.data['username'], email=serializer.data['email'], password=serializer.data['password'],**kwargs)
            token=get_tokens_for_user(user)
            headers = self.get_success_headers(serializer.data)
            return Response({'token':token,'msg':'registration succeed'},status=status.HTTP_201_CREATED,headers=headers)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
class UserLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid(raise_exception=True):
            username=serializer.data.get("username")
            password=serializer.data.get("password")
            print(f'username is {username} password is {password}')
            user=authenticate(username=username,password=password)
            login(request,user)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({"tokens":token,"msg":"login sucessfull"})
            else:
                return Response({"error":"username or password is not valid"},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    