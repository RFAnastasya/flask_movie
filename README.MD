# Новостной портал

Портал для публикации отзывов на фильмы и их оценок.

## Описание
Сайт с фильмами, созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro.

## Технологии
* Python
* Flask
* WTForms
* SQLAlchemy
* werkzeug.utils

## Как запустить

1. Склонируйте репозиторий
2. Создайте и активируйте виртаульное окружение
```commandline
python -m venv venv
source venv/Scripts/activate
```  
3. Установите зависимости
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env и укажите настройки подключения к БД и другие параметры.
```commandline
DATABASE_URI = sqlite:///movie.db
SECRET_KEY = SECRET_KEY
```
5. Запустите flask приложение
```commandline
flask run
```

## Автор
Рыбак А.