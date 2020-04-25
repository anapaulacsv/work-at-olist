from .models import Author, Book
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.filters import BaseFilterBackend

class AuthorFilter(BaseFilterBackend):
    """
    Custom filter of author
    """
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset    

class BookFilter(BaseFilterBackend):
    """
    Custom filter of book
    """
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        edition = request.query_params.get('edition', None)
        pub_year = request.query_params.get('pub_year', None)
        author_name = request.query_params.get('author_name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if edition is not None:
            queryset = queryset.filter(edition=edition)
        if pub_year is not None:
            queryset = queryset.filter(pub_year=pub_year)
        if author_name is not None:
            queryset = queryset.filter(authors__name__icontains=author_name)
        return queryset  

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [AuthorFilter]
    #Login required
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [BookFilter]
    #Login required
    permission_classes = [permissions.IsAuthenticated]      