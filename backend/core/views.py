from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from recipes.models import Recipes

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


User = get_user_model()


class UserRecipesViewSet(APIView):
    queryset = None
    serializer = None
    message = ''
    message_plural = ''

    @action(
        methods=['post'],
        detail=True,
    )
    def post(self, request, recipe_id):
        user_id = request.user.id
        if self.queryset.filter(
            user=user_id,
            recipes=recipe_id
        ).exists():
            return Response(
                {'Ошибка': f'Ошибка добавления в {self.message}'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            'user': user_id,
            'recipes': recipe_id,
        }
        serializer = self.serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return_page = Recipes.objects.filter(pk=recipe_id).values(
            'id',
            'name',
            'image',
            'cooking_time',
        ).first()
        return Response(
            return_page,
            status=status.HTTP_201_CREATED
        )

    @action(
        methods=['delete'],
        detail=True,
    )
    def delete(self, request, recipe_id):
        user_id = request.user.id
        recipe = get_object_or_404(Recipes, pk=recipe_id)
        if not self.queryset.filter(
            user=user_id,
            recipes=recipe
        ).exists():
            return Response(
                {'Ошибка': f'Рецепта нет в {self.message_plural}'},
                status=status.HTTP_400_BAD_REQUEST)
        self.queryset.get(
            user=user_id,
            recipes=recipe
        ).delete()
        return Response(
            {'Ошибка': 'Рецепт успешно удален'},
            status=status.HTTP_204_NO_CONTENT
        )
