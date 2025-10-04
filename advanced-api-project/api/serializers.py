from rest_framework import serializers
from .models import Author, Book
import datetime

"""
Serializers transform our model instances into JSON
and also validate incoming request data.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Custom validation:
        Ensure that publication year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: show books inside author response
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
