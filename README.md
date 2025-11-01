
# Recipes Django Project (minimal)

Этот проект — минимальная заготовка **Django** приложения для кулинарного сайта:
- Категории, теги, рецепты с изображением (ImageField)
- Комментарии
- Админка (добавление рецептов/тегов/категорий и удаление комментариев)
- Поиск по названию и тегам (поле `q` в форме поиска)
- Использует SQLite (чтобы сразу запускалось локально)

**Как запустить локально**
1. Создайте виртуальное окружение (рекомендуется):
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Linux / macOS
   .venv\Scripts\activate     # Windows
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Выполните миграции и создайте суперпользователя:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
5. Откройте http://127.0.0.1:8000/ — главная страница.
6. Админка: http://127.0.0.1:8000/admin/

**Деплой на Render**
- Залейте репозиторий на GitHub, подключите к Render.
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn recipes_project.wsgi`
- У Render обязательно настраивать хранение медиа (S3/Cloudinary) — по умолчанию Render не хранит пользовательские файлы стабильно.

