from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        model = Book
        fields = [
        'id',
        'owner',
        'title',
        'author',
        'link',
        'created_at',
        'profile_id',
        'profile_image'
        ]
        read_only_fields = ['owner', 'created_at']
