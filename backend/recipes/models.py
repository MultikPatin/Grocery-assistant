from django.contrib.auth import get_user_model
from django.db import models

from core.models import (
    NameMixinModel,
    RecipesMixinModel,
    UserRecipes
)

User = get_user_model()


class Ingredients(NameMixinModel):
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=10,
        help_text='Введите единицу измерения'
    )

    class Meta:
        db_table = 'ingredients'
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'


class Tags(NameMixinModel):
    color = models.CharField(
        'Цвет',
        max_length=16,
        help_text='Введите цвет'
    )
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'тэг'
        verbose_name_plural = 'теги'


class Recipes(NameMixinModel):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='автор',
        help_text='Выберите автора'
    )
    ingredients = models.ManyToManyField(
        Ingredients,
        through='IngredientsRecipes',
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tags,
        through='TagsRecipes',
        related_name='recipes'
    )
    image = models.ImageField(
        upload_to='recipes/images/',
        null=True,
        default=None,
        verbose_name='Изображение',
        help_text='Выберите изображение'
    )
    text = models.TextField(
        verbose_name='описание',
        help_text='Введите описание'
    )
    cooking_time = models.IntegerField(
        verbose_name='время приготовления',
        help_text='Введите время приготовления в минутах'
    )

    class Meta:
        db_table = 'recipes'
        ordering = ['id']
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'


class IngredientsRecipes(RecipesMixinModel):
    ingredients = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        related_name='ingredientsrecipes',
        verbose_name='ингредиент',
        help_text='Выберите ингредиент'
    )
    amount = models.IntegerField(
        verbose_name='количество',
        help_text='Введите количество'
    )

    class Meta:
        db_table = 'ingredientsrecipes'
        ordering = ['recipes']
        verbose_name = 'строки ингредиентов к рецептам'
        verbose_name_plural = 'рецепты -> ингредиенты'


class TagsRecipes(RecipesMixinModel):
    tags = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE,
        related_name='tagsrecipes',
        verbose_name='тег',
        help_text='Выберите тег'
    )

    class Meta:
        db_table = 'tagsrecipes'
        ordering = ['recipes']
        verbose_name = 'строки тегов к рецептам'
        verbose_name_plural = 'рецепты -> теги'


class Favorite(UserRecipes):

    class Meta:
        db_table = 'favorite'
        ordering = ['user']
        verbose_name = 'избранное'
        verbose_name_plural = 'рецепты -> избранное'


class ShoppingCart(UserRecipes):

    class Meta:
        db_table = 'shoppingcart'
        ordering = ['user']
        verbose_name = 'корзину'
        verbose_name_plural = 'рецепты -> корзина'
