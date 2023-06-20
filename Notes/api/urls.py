
from django.contrib import admin
from django.urls import path,include
from .views import CreateNoteAPIView
urlpatterns = [
    path('create',CreateNoteAPIView.as_view(),name='create note')
]
