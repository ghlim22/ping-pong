from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

# Create your views here.


@api_view(["GET"])
def hello(request):
    return Response("hello world!")


class HelloAPI(APIView):
    def get(self, request):
        return Response("hello, world!")


# Function based view


@api_view(["GET", "POST"])
def booksAPI(request):  # /book/
    if request.method == "GET":  # GET request for the whole books.
        books = Book.objects.all()  # Get all objects from Book model.
        serializer = BookSerializer(books, many=True)  # Put all books into serializer.
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":  # POST request for register a book information.
        serializer = BookSerializer(data=request.data)  # Put data from request into serializer
        if serializer.is_valid():
            serializer.save()  # Deserialize using create().
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def bookAPI(request, pk):  # /book/book_id/
    book = get_object_or_404(Book, pk=pk)  # Get the requested object.
    serializer = BookSerializer(book)  # Serialize
    return Response(serializer.data, status=status.HTTP_200_OK)


# Class based view


class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPI(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
