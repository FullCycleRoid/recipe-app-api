from .serializers import UserSerializers
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializers