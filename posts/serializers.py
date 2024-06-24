from rest_framework import serializers
from posts.models import Post, Ingredient
from likes.models import Like

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'measurement')


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    ingredients = IngredientSerializer(many=True, source='ingredients.all')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        post = Post.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(post=post, **ingredient_data)
        return post

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        instance = super().update(instance, validated_data)
        current_ingredient_ids = instance.ingredients.values_list('id', flat=True)
        for ingredient_data in ingredients_data:
            if 'id' in ingredient_data:
                ingredient = Ingredient.objects.get(id=ingredient_data['id'], post=instance)
                ingredient.name = ingredient_data.get('name', ingredient.name)
                ingredient.quantity = ingredient_data.get('quantity', ingredient.quantity)
                ingredient.measurement = ingredient_data.get('measurement', ingredient.measurement)
                ingredient.save()
            else:
                Ingredient.objects.create(post=instance, **ingredient_data)
        # Delete ingredients not included in ingredients_data
        instance.ingredients.exclude(id__in=current_ingredient_ids).delete()
        return instance

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'recipe_name', 'description', 'image', 'like_id',
            'likes_count', 'comments_count', 'ingredients',
        ]
