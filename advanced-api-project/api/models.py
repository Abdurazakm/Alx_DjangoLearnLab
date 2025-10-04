from django.db import models

"""
Models for Author and Book.

Author -> One author can have many books.
Book -> Each book is linked to exactly one author.
"""

class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the author")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE,
        help_text="Author of this book"
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
