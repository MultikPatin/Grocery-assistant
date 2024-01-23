from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Follow


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
    )
    list_editable = (
        'username',
        'first_name',
        'last_name',
    )
    search_fields = ('username',)
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'following',
    )
    search_fields = ('user',)
    empty_value_display = '-пусто-'
