from .models import Author, Book
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.filters import BaseFilterBackend

class AuthorFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(name="Batman")

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [AuthorFilter] 
    #Login required
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Login required
    permission_classes = [permissions.IsAuthenticated]      