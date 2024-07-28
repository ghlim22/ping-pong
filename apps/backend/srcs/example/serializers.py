from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = [
            "book_id",
            "title",
            "author",
            "category",
            "pages",
            "price",
            "publication_date",
            "description",
        ]
