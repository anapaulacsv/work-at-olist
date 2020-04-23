from .models import Author, Book
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer

# 

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    #Login required
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Login required
    permission_classes = [permissions.IsAuthenticated]      