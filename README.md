# Library 

## Описание

**Library** — это веб-приложение, разработанное на Django, которое предоставляет функционал для управления библиотекой. Система позволяет пользователям, зарегистрированным как Читатели, просматривать каталог книг, брать книги на время и возвращать их. Библиотекари могут просматривать список должников.

## Функциональные возможности

- **Аутентификация и авторизация**: Пользователи могут регистрироваться, входить в систему и обновлять свои профили.
- **Каталог книг**: Просмотр доступных книг с возможностью взять книгу.
- **Взятие и возврат книг**: Читатели могут брать книги и возвращать их.
- **Управление профилем**: Пользователи могут обновлять свои личные данные.
- **Роли пользователей**: Две роли — Читатель и Библиотекарь. Библиотекари могут управлять библиотекой и просматривать список должников.

## Установка

### Шаги установки

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/your-username/library.git
   cd library

2. **Создание и активация виртуального окружения**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте venv\Scripts\activate

3. **Установка зависимостей**

   ```bash
   pip install -r requirements.txt

4. **Применение миграций**
   
   Выполните миграции для создания необходимых таблиц в базе данных:

   ```bash
   python manage.py migrate

5. **Создание суперпользователя**

   Создайте суперпользователя для доступа к административной панели:
   ```bash
   python manage.py createsuperuser

6. **Запуск сервера**

   ```bash
   python manage.py runserver #http://localhost:8000
 
   

   
