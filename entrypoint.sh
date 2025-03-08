#!/bin/bash
set -e

# Для отладки
echo "Current environment:"
echo "PYTHONPATH: $PYTHONPATH"
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"

# Проверяем Python после активации
echo "Python executable after activation: $(which python)"
echo "Python path after activation: $(python -c 'import sys; print(sys.path)')"

# Проверяем установленные пакеты
echo "Installed packages:"
python -m pip list

# Проверяем, что Django установлен
# echo "Checking Django installation:"
# python -m pip list | grep django
# python -c "import django; print(f'Django version: {django.get_version()}')"

# Запускаем миграции
echo "Running migrations..."
python src/frameworks_and_drivers/django/manage.py migrate

# Запускаем сервер
echo "Starting server..."
python src/frameworks_and_drivers/django/manage.py runserver 0.0.0.0:8020