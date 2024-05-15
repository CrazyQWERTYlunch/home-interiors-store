# Проект: Магазин мебели Home
Этот репозиторий содержит исходный код для проекта, который представляет собой веб-приложение для магазина мебели Home.

## Технологии
Django, Bootstrap, PostgreSQL, jQuery

## Установка
1. Клонируйте репозиторий на локальную машину:
    ```bash
    git clone https://github.com/CrazyQWERTYlunch/home-interiors-store.git
    ```
2. Установите зависимости Python, используя pip:
    ```bash
    pip install -r requirements.txt
    ```
3. Настройте базу данных PostgreSQL в файле settings.py вашего проекта
4. Выполните миграции для создания необходимых таблиц в базе данных:
    ```bash
       python manage.py migrate
    ```
5. Заполните базу данных данными с помощтю комманд:
    ```bash
    python manage.py loaddata fixtures/goods/categories.json
    
    python manage.py loaddata fixtures/goods/products.json
    ```
6. Запустите сервер разработки Django с помощью команды:
    ```bash
    python manage.py runserver
    ```