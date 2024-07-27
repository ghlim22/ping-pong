from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


@api_view(["GET"])
def hello(request):
    return Response("hello world!")
