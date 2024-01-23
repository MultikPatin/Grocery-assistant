from django.contrib import admin

from .models import (
    Favorite,
    Ingredients,
    IngredientsRecipes,
    Recipes,
    ShoppingCart,
    Tags,
    TagsRecipes,
)


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'image',
        'text',
        'cooking_time',
    )
    list_editable = (
        'name',
        'text',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    list_editable = ('name', 'measurement_unit',)
    search_fields = ('name',)
    list_filter = ('measurement_unit',)
    empty_value_display = '-пусто-'


@admin.register(Tags)
class TagssAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug',
    )
    list_editable = ('name', 'color',)
    search_fields = ('name',)
    list_filter = ('color',)
    empty_value_display = '-пусто-'


@admin.register(IngredientsRecipes)
class IngredientsRecipesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ingredients',
        'recipes',
        'amount',
    )
    list_editable = (
        'ingredients',
        'amount',
    )
    search_fields = ('recipes',)
    empty_value_display = '-пусто-'


@admin.register(TagsRecipes)
class TagsRecipesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tags',
        'recipes',
    )
    list_editable = (
        'tags',
    )
    search_fields = ('recipes',)
    empty_value_display = '-пусто-'


class ListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipes',
    )
    search_fields = ('user',)
    empty_value_display = '-пусто-'


@admin.register(Favorite)
class FavoriteAdmin(ListAdmin):
    pass


@admin.register(ShoppingCart)
class ShoppingCartAdmin(ListAdmin):
    pass
