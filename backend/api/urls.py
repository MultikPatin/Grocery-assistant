from django.urls import include, path, re_path

from recipes.views import (
    FavoriteView,
    IngredientsViewSet,
    RecipesViewSet,
    ShoppingCartViewSet,
    TagsViewSet,
    download_shopping_cart,
)

from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

router = DefaultRouter()
router.register('recipes',
                RecipesViewSet,
                basename='recipes')
router.register('tags',
                TagsViewSet,
                basename='tags')
router.register('ingredients',
                IngredientsViewSet,
                basename='ingredients')
router.register('users',
                CustomUserViewSet,
                basename='recipes')
urlpatterns = [
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path(
        'recipes/download_shopping_cart/',
        download_shopping_cart,
        name='download',
    ),
    path(
        'recipes/<int:recipe_id>/favorite/',
        FavoriteView.as_view(),
    ),
    path(
        'recipes/<int:recipe_id>/shopping_cart/',
        ShoppingCartViewSet.as_view(),
    ),
    path('', include(router.urls)),
]
