<img src="icon.png" align="right" />

# Описание проекта Api_Yatube

Проект представляет собой социальную сеть для публикации личных дневников. 
Реализован API для всех моделей приложения. По запросу можно просмотреть все записи автора.
Пользователи могут делать запросы к чужим страницам, комментировать записи различных авторов, подписываться на них.
API доступен только аутентифицированным пользователям. Реализованы возможность фильтрации и сортировки данных в выдаче.
Добавлена пагинация ответов.

# Используемые технологии

Python 3.9, Django 2.2 LTS, Django ORM, Django REST Framework (DRF), REST API, SQLite3, CSRF, Paginator, Simple-JWT, Djoser

## Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Trohimets/api_final_yatube.git
```
```
cd api_final_yatube
```
- Cоздать и активировать виртуальное окружение:
```
py -m venv venv
```
```
source venv/scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```

## Настроены такие эндпоинты:

```
    api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
    api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
    api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
    api/v1/groups/ (GET): получаем список всех групп.
    api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
    api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или 
    создаём новый, указав id поста, который хотим прокомментировать.
    api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или 
    удаляем комментарий по id у поста с id=post_id.
```
## Примеры запросов:

```
- Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
POST .../api/v1/posts/
```
- Пример ответа:
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
} 
```
- Пример GET-запроса: получаем информацию о группе.
GET .../api/v1/groups/2/

- Пример ответа:
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
```
# Разработчики

[Трохимец Константин](https://github.com/Trohimets): весь проект.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
