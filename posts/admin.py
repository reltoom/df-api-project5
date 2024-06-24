from django.contrib import admin
from .models import Post, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

    list_display = ('id', 'recipe_name', 'owner', 'created_at', 'updated_at')
    list_filter = ('owner', 'created_at', 'updated_at')
    search_fields = ('recipe_name', 'owner__username')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'measurement', 'post')
    list_filter = ('post',)
    search_fields = ('name', 'post__recipe_name')