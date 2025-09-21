from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only logged-in users can access
class AdminOnlyBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
### Authentication & Permissions
# - Authentication: Token-based (`rest_framework.authtoken`)
# - To obtain a token, POST username/password to `/api-token-auth/`
# - Use `Authorization: Token <your-token>` header for all requests
# - Default permissions: `IsAuthenticated`
# - BookViewSet requires authenticated users to access CRUD endpoints
