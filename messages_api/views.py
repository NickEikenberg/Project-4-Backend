from django.shortcuts import render
from rest_framework import generics
from .serializers import MessageSerializer
from .models import Message

# Create your views here.

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer