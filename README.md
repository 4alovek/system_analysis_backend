# system_analysis_backend


**Проект** — это мобильное приложение с умной лентой новостей, которая генерирует контент на основе интересов пользователей. Приложение использует интеграцию с GPT API для создания персонализированных постов.

---

## Оглавление

1. [Описание проекта](#описание-проекта)
2. [Технологии](#технологии)
3. [Структура проекта](#структура-проекта)
4. [Установка и запуск](#установка-и-запуск)
5. [Настройка переменных окружения](#настройка-переменных-окружения)
6. [Использование API](#использование-api)
7. [Развертывание](#развертывание)

---

## Описание проекта

Приложение позволяет пользователям:
- Создавать учетные записи и указывать свои интересы.
- Получать персонализированную ленту новостей.
- Запрашивать генерацию постов через GPT API.
- Реагировать на посты (лайки/дизлайки).

Ключевые особенности:
- **Персонализация**: Контент генерируется на основе интересов пользователя.
- **Интеграция с GPT**: Автоматическая генерация постов с использованием GPT API.
- **Чистая архитектура**: Проект организован по принципам Clean Architecture для удобства поддержки и масштабирования.

---

## Технологии

- **Backend**: Django, Django REST Framework
- **База данных**: PostgreSQL
- **API**: RESTful API
- **Интеграция с GPT**: OpenAI GPT API

---

## Структура проекта

```
project/
└── src/
    ├── entities/                     # Бизнес-сущности
    ├── frameworks_and_drivers/       # Реализация фреймворков и драйверов
    │   ├── django/backend            # Django-приложения
    │   │   ├── apps/                 # Логические модули: users, posts, gpt_integration
    │   │   ├── manage.py             # Управление Django
    │   │   ├── settings.py           # Настройки проекта
    │   │   ├── urls.py               # Маршруты API
    │   ├── repositories_implementations/  # Реализации репозиториев
    │   └── interface_adapters/       # Адаптеры для взаимодействия с интерфейсами
    │       ├── controllers/          # Контроллеры
    │       ├── dtos/                 # DTO (Data Transfer Objects)
    │       ├── presenters/           # Представления данных
    │       └── repositories_interfaces/  # Интерфейсы репозиториев
    └── usecases/                     # Бизнес-логика (Use Cases)
```

---

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/4alovek/system_analysis_backend.git
cd system_analysis_backend
```

### 2. Установка зависимостей
```bash
poetry install
```

### 3. Настройка подключение к GPT-модели находится в файле
```bash
-  `src/frameworks_and_drivers/django/gpt_integration/gpt_service.py`
```

### 4. Настройка базы данных
Создайте базу данных PostgreSQL и примените миграции:
```bash
python manage.py migrate
```

### 5. Запуск сервера разработки
```bash
python frameworks_and_drivers/django/manage.py runserver
```

Приложение будет доступно по адресу: `http://127.0.0.1:8000/`.

---

## Использование API

### 1. Регистрация пользователя
**POST** `/api/users/register/`
```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "full_name": "John Doe"
}
```

### 2. Авторизация
**POST** `/api/users/login/`
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

### 3. Генерация поста
**POST** `/api/posts/generate/`
```json
{
  "prompt": "Write a post about AI in healthcare."
}
```

### 4. Получение ленты новостей
**GET** `/api/posts/feed/`
