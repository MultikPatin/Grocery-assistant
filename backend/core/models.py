from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class NameMixinModel(models.Model):
    name = models.CharField(
        'название',
        max_length=200,
        unique=True,
        help_text='Введите название'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RecipesMixinModel(models.Model):
    recipes = models.ForeignKey(
        to='recipes.Recipes',
        on_delete=models.CASCADE,
        verbose_name='рецепт',
        help_text='Выберите рецепт'
    )

    class Meta:
        abstract = True


class UserRecipes(RecipesMixinModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        help_text='Выберите пользователя'
    )

    class Meta:
        abstract = True
