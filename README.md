# prog_for_linguists
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