from rest_framework import serializers
from .models import Author, Book

# -------------------------------
# Book Serializer
# -------------------------------
class BookSerializer(serializers.ModelSerializer):
    # 🔹 Add relationship fields for Task 2
    # By ID (used for creating/updating a book)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source="author"
    )
    # By name (read-only)
    author_name = serializers.StringRelatedField(source="author", read_only=True)
    # Nested author details (read-only)
    author_details = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "publication_year",
            "author_id",
            "author_name",
            "author_details",
        ]

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        import datetime
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    # Return nested author details
    def get_author_details(self, obj):
        return AuthorSerializer(obj.author).data


# -------------------------------
# Author Serializer
# -------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    # Show books related to this author
    books = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
