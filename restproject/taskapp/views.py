from django.shortcuts import render
from .serializers import Taskserializers,UserSerializers
from .models import Rides
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


# Create your views here.


class Taskviewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    queryset = Rides.objects.all()
    serializer_class = Taskserializers


class CreateuserView(generics.CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers
