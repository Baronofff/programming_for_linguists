# Транскрибация аудиофайлов (.wav → .txt)
Этот проект предоставляет простой и удобный веб-сервис для транскрибации аудиофайлов в формате .wav в текстовые файлы .txt с использованием библиотек для распознавания речи.

# Использование
Отправьте POST-запрос на /transcribe с аудиофайлом .wav в теле запроса.
В ответ вы получите текстовую транскрипцию.

# Основные технологии
- Python 3.12+
- FastAPI — для создания API
- SpeechRecognition — для обработки аудио и преобразования речи в текст

# Cтруктура проекта
programming_for_linguists/
├── src/

│   ├── api/

│   │   ├── endpoints/

│   │   │   ├── __init__.py

│   │   │   └── routers.py

│   │   └── validators.py

│   ├── services/

│   │   ├── __init__.py

│   │   └── transcription.py

│   ├── __init__.py

│   └── main.py

├── .gitignore

├── LICENSE

├── poetry.lock

├── pyproject.toml

└── README.md


# Разработка
## Управление зависимостями

Для управления зависимостями используется пакет `Poetry`

### Установка poetry
В глобальном окружении выполните:

#### Для Windows:
```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
или
```shell
pip install poetry
```

#### Для Linux / MacOS:
```shell
pip install poetry
```
или
```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Затем чтобы Poetry создавал виртуальное окружение в папке проекта выполните:
```shell
poetry config virtualenvs.in-project true
```

Проверить установку параметра virtualenvs.in-project = true можно командой:
```shell
poetry config --list
```

### Перейдите в корневую папку проекта:

Установка зависимостей:
```shell
poetry install
```

Показать установленные пакеты:
```shell
poetry show
```
или
```shell
poetry show --tree
```

### Ваше виртуальное окружение настроено и готово к работе!

#### Вы можете использовать его двумя способами:

Активировать оболочку, в таком случае все инструменты будут запускаться в виртуальной среде:
```shell
poetry shell
```

или разово запускать определенные файлы и инструменты в виртуальной среде с помощью:
```shell
poetry run python <your_script.py>
```

## Стилистика

Для стилизации кода используется пакет `Ruff`

Проверка стилистики кода осуществляется командой
```shell
ruff check
```

Если одновременно надо пофиксить то, что можно поиксить автоматически, то добавляем параметр `--fix`
```shell
ruff check --fix
```

Что бы стилистика автоматически проверялась и поправлялась при комитах надо добавить hook pre-commit к git

```shell
pre-commit install
```