from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User1

"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('Real_name')
    serializer_class = UserSerializer

    """
class UserViewSet(viewsets.ModelViewSet):
    queryset = User1.objects.all()
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
