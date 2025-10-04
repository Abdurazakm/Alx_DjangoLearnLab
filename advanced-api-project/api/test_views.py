from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITests(APITestCase):
    def setUp(self):
        # Create user for authentication
        self.user = User.objects.create_user(username="user1", password="pass1234")
        self.client = APIClient()
        self.client.login(username="user1", password="pass1234")

        # Create author instance
        self.author = Author.objects.create(name="John Doe")

        # Create books with the Author model
        self.book1 = Book.objects.create(title="Python Basics", author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", author=self.author, publication_year=2023)

        # URLs (make sure names match your urls.py)
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])
     # ---- CRUD TESTS ----
    def test_create_book_authenticated(self):
        data = {
            "title": "New Book",
            "author": self.user.id,
            "publication_year": 2024
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "author": self.user.id,
            "publication_year": 2025
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book_authenticated(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---- FILTER, SEARCH, ORDER TESTS ----
    def test_filter_books_by_publication_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2020")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Python Basics")

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Advanced Django")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ["Advanced Django", "Python Basics"])


    def test_create_book_authenticated(self):
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2024
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
