from rest_framework import generics,status
from django.contrib.auth.models import User
from .serializers import CreateNoteSerializer
from Notes.models import Note
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
class CreateNoteAPIView(generics.CreateAPIView):
    serializer_class = CreateNoteSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication,BaseAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
