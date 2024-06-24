from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'recipe_name',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        ingredients_data = self.request.data.pop('ingredients', [])
        serializer = PostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save(owner=self.request.user)

        for ingredient_data in ingredients_data:
            Ingredient.objects.create(post=post, **ingredient_data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    def perform_update(self, serializer):
        ingredients_data = self.request.data.pop('ingredients', [])
        instance = serializer.save()

        # Clear existing ingredients and create new ones
        instance.ingredients.all().delete()
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(post=instance, **ingredient_data)

    def perform_destroy(self, instance):
        # Delete associated ingredients when deleting a post
        instance.ingredients.all().delete()
        instance.delete()
