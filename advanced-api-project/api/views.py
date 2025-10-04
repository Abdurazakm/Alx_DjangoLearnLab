from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
Views for Book model using Django REST Framework's generic views.
This provides CRUD functionality with minimal boilerplate code.
"""

# List all books / Create a new book
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Read for everyone, write only for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()

# Retrieve / Update / Delete a book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Read for everyone, write only for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
