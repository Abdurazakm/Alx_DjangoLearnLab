from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters

from .models import Book
from .serializers import BookSerializer

# ✅ List + Filtering + Searching + Ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Unauthenticated users can view only

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter
    ]

    # Filter by exact match
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search by text (partial match, case-insensitive)
    search_fields = ['title', 'author__name']

    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


# ✅ Retrieve one book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view details


# ✅ Create a book (Auth required)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ✅ Update a book (Auth required)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ✅ Delete a book (Auth required)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
