![repo size](https://img.shields.io/github/repo-size/foxygen-d/cat_charity_fund)
![py version](https://img.shields.io/pypi/pyversions/3)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)

# Продуктовый помощник

![alt text](https://pictures.s3.yandex.net/resources/S16_01_1692340098.png)

### Описание проекта

Проект реализует сайт кулинарных рецептов,
в котором вы можете создавать рецепты, подписываться на понравившихся
авторов, подобрать себе коллекцию любимых рецептов и другой функционал.



## Запуск проекта


### Проект запускается в 4 контейнерах

    nginx
    backend
    frontend
    db

### Авторизация по токену

Все запросы от имени пользователя должны выполняться с заголовком

    "Authorization: Token TOKENVALUE"

### Необходимые инструменты для запуска

    docker

### Запуск приложения

Перед запуском необходимо создать файл .env с переменными в
корневом каталоге

    POSTGRES_DB
    POSTGRES_USER
    POSTGRES_PASSWORD
    DB_HOST
    DB_PORT
    SECRET_KEY
    ALLOWED_HOSTS
    DEBUG

### Запуск контейнеров

Перейти в каталог /infra/ и выполнить

```bash
docker-compose up -d --build
```

При запуске контейнеров БД создаётся автоматически и так же теги и
ингредиенты автоматически заполняются данными из файлов:

    /backend/test_data/ingredients.csv
    /backend/test_data/tags.csv


### Стек используемых технологий

    Python 3.9
    Django 4.2.3
    djangorestframework 3.14.0
    Docker
    PostgreSQL 13.10
    gunicorn 20.1.0
    CI
    nginx 1.19.3
    djoser 2.2.0

## Доступные эндпоинты

#### docs

            docs/                           # Документация проекта

#### admin

            admin/                          # Панель администратора

#### recipes

    GET     recipes/                        # Получить список рецептов
    POST    recipes/                        # Создание рецепта
    GET     recipes/{id}/                   # Получение рецепта по id
    PATCH   recipes/{id}                    # Изменение рецепта
    DELETE  recipes/{id}/                   # Удаление рецепта
    GET     recipes/download_shopping_cart/ # Скачать список покупок
    POST    recipes/{id}/shopping_cart      # Добавить рецепт в список покупок
    DELETE  recipes/{id}/shopping_cart      # Удаление рецепта из списка покупок
    POST    recipes/{id}/favorite/          # Добавить рецепт в избранное
    DELETE  recipes/{id}/favorite/          # Удаление рецепта из избранного

#### users

    POST    users/                          # Регистрация пользователя
    GET     users/                          # Получение списка пользователей
    GET     users/{id}/                     # Получение пользователя по id
    GET     users/me/                       # Получение текущего пользователя
    POST    users/set_password/             # Изменение пароля текущего пользователя
    GET     users/subscriptions/            # Мои подписки
    POST    users/{id}/subscribe/           # Подписаться на пользователя
    DELETE  users/{id}/subscribe/           # Отписаться от пользователя
    POST    auth/token/login/               # Получить токен авторизации
    POST    auth/token/logout/              # Удаление токена

#### ingredients

    GET     ingredients/                    # Получить список ингредиентов
    GET     ingredients/{id}/               # Получить ингредиент по id

#### tags

    GET     tags/                           # Получить список ингредиентов
    GET     tags/{id}/                      # Получение тега по id
