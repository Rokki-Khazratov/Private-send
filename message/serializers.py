import random
import string
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def generate_random_slug(self):
        length = 8
        chars = string.ascii_letters + string.digits
