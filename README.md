# ДЗ 1 YLab_University 

## Установка и запуск

#### Скачать проект
```bash
git clone git@github.com:ProtKsen/ylab_task_menu.git
```

#### Установка poetry, выполняется один раз
```bash
pip install poetry
poetry config virtualenvs.in-project true
```

#### Установка зависимостей
```bash
poetry install
```

#### Настройки окружения
Создать файл `.env` на базе `.env.default`.

#### Установка docker, выполняется один раз
См. <https://docs.docker.com/engine/install/>

#### Установка uvicorn, выполняется один раз
```bash
pip install uvicorn
```

#### Запуск базы данных
```bash
make db.run
```

#### Выполнить миграции
```bash
make db.migrate
```

#### Запуск приложения
```bash
make app.run
```
