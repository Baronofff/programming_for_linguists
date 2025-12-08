# 1. Базовый образ с Python
FROM python:3.12-slim

# 2. Рабочая директория внутри контейнера
WORKDIR /src

# 3. Установка Poetry
RUN pip install --no-cache-dir poetry==2.2.1
RUN pip install uvicorn

# 4. Копируем файлы Poetry
COPY pyproject.toml poetry.lock ./

# 5. Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false
RUN poetry install --without dev

# 6. Копируем наш проект внутрь контейнера
COPY src/ ./src/

# 7. Определяем поведение контейнера при запуске
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]