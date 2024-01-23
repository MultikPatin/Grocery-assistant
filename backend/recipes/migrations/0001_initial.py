# Generated by Django 4.2.3 on 2023-07-25 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'избранное',
                'verbose_name_plural': 'рецепты -> избранное',
                'db_table': 'favorite',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=200, unique=True, verbose_name='название')),
                ('measurement_unit', models.CharField(help_text='Введите единицу измерения', max_length=10, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'ингредиент',
                'verbose_name_plural': 'ингредиенты',
                'db_table': 'ingredients',
            },
        ),
        migrations.CreateModel(
            name='IngredientsRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(help_text='Введите количество', verbose_name='количество')),
            ],
            options={
                'verbose_name': 'строки ингредиентов к рецептам',
                'verbose_name_plural': 'рецепты -> ингредиенты',
                'db_table': 'ingredientsrecipes',
                'ordering': ['recipes'],
            },
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=200, unique=True, verbose_name='название')),
                ('image', models.ImageField(default=None, help_text='Выберите изображение', null=True, upload_to='recipes/images/', verbose_name='Изображение')),
                ('text', models.TextField(help_text='Введите описание', verbose_name='описание')),
                ('cooking_time', models.IntegerField(help_text='Введите время приготовления в минутах', verbose_name='время приготовления')),
            ],
            options={
                'verbose_name': 'рецепт',
                'verbose_name_plural': 'рецепты',
                'db_table': 'recipes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=200, unique=True, verbose_name='название')),
                ('color', models.CharField(help_text='Введите цвет', max_length=16, verbose_name='Цвет')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'теги',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TagsRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipes', models.ForeignKey(help_text='Выберите рецепт', on_delete=django.db.models.deletion.CASCADE, to='recipes.recipes', verbose_name='рецепт')),
                ('tags', models.ForeignKey(help_text='Выберите тег', on_delete=django.db.models.deletion.CASCADE, related_name='tagsrecipes', to='recipes.tags', verbose_name='тег')),
            ],
            options={
                'verbose_name': 'строки тегов к рецептам',
                'verbose_name_plural': 'рецепты -> теги',
                'db_table': 'tagsrecipes',
                'ordering': ['recipes'],
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipes', models.ForeignKey(help_text='Выберите рецепт', on_delete=django.db.models.deletion.CASCADE, to='recipes.recipes', verbose_name='рецепт')),
            ],
            options={
                'verbose_name': 'корзину',
                'verbose_name_plural': 'рецепты -> корзина',
                'db_table': 'shoppingcart',
                'ordering': ['user'],
            },
        ),
    ]