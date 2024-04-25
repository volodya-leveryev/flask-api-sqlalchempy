# Пример API на базе Flask

Использованные библиотеки:

* [Flask](https://flask.palletsprojects.com/)
* [Flask-RESTX](https://flask-restx.readthedocs.io/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
* [Coverage.py](https://coverage.readthedocs.io/)
* [pytest](https://docs.pytest.org/)

## Порядок действий

1. Склонировать репозиторий
2. Создать и активировать виртуальное окружение
3. Установить библиотеки
4. Выполнить в интерактивной оболочке Python:

```
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
```

5. Открыть созданный файл test.db в средстве просмотра SQLite и добавить несколько строк данных
6. Запустить сервер Flask в отладочном режиме:

```
flask run --debug
```

7. Проверить работу REST API и GraphQL
8. Добавить в GraphQL запрос и резолвер для получение списка всех книг
