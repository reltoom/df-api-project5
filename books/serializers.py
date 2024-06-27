from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'owner', 'title', 'author', 'link', 'created_at']
        read_only_fields = ['owner', 'created_at']