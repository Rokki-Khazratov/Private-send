import random
import string
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def generate_random_slug(self):
        length = 8
        chars = string.ascii_letters + string.digits
        slug = ''.join(random.choice(chars) for _ in range(length))
        return slug

    def perform_create(self, serializer):
        slug = self.generate_random_slug()
        serializer.save(slug=slug)

class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'slug'