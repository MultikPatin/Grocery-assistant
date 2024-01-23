from django.contrib.auth import get_user_model
from django.http import HttpResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import (
    SAFE_METHODS,
    IsAuthenticatedOrReadOnly,
)
from .models import (
    Ingredients,
    Tags,
    Recipes,
    Favorite,
    ShoppingCart,
    IngredientsRecipes,
)
from .serializers import (
    IngredientSerializer,
    TagsSerializer,
    RecipesSerializer,
    RecipesSafeMethodSerializer,
    FavoriteSerializer,
    ShoppingCartSerializer
)
from core.views import UserRecipesViewSet

from api.permissions import AuthorOrReadOnly
from api.filters import (
    RecipesFilter,
    IngredientsFilter
)


User = get_user_model()


class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_class = IngredientsFilter


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    permission_classes = [AuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipesFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipesSafeMethodSerializer
        return RecipesSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            'Рецепт успешно удален',
            status=status.HTTP_204_NO_CONTENT
        )


class FavoriteView(UserRecipesViewSet):
    queryset = Favorite.objects.all()
    serializer = FavoriteSerializer
    message = 'избранное'
    message_plural = 'избранном'


class ShoppingCartViewSet(UserRecipesViewSet):
    queryset = ShoppingCart.objects.all()
    serializer = ShoppingCartSerializer
    message = 'список покупок'
    message_plural = 'списке покупок'


@api_view(['GET'])
def download_shopping_cart(request):
    shopping_cart = ShoppingCart.objects.filter(
        user=request.user
    )
    buying_list = {}
    for record in shopping_cart:
        ingredients = IngredientsRecipes.objects.filter(
            recipes=record.recipes
        )
        for ingredient in ingredients:
            amount = ingredient.amount
            name = ingredient.ingredients.name
            measurement_unit = ingredient.ingredients.measurement_unit
            if name not in buying_list:
                buying_list[name] = {
                    'measurement_unit': measurement_unit,
                    'amount': amount,
                }
            else:
                buying_list[name]['amount'] = (
                    buying_list[name]['amount'] + amount
                )

    with open('/media/shopping_cart.txt', 'w+', encoding='utf8') as card:
        for name, data in buying_list.items():
            amount = data['amount']
            measurement_unit = data['measurement_unit']
            card.write(
                f'{name} - {amount} {measurement_unit}\n'
            )

    data = open('/media/shopping_cart.txt', 'r').read()
    response = HttpResponse(
        data,
        content_type='text/plain',
        status=status.HTTP_200_OK
    )
    response['Content-Disposition'] = (
        'attachment; filename="shopping_cart.txt"')
    return response
