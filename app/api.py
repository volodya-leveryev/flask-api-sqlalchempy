from flask import request
from flask_restx import Api, Resource

from app.models import Book, db

api = Api()


class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return book.to_dict()

    def put(self, book_id):
        data = request.get_json()

        # TODO: валидация данных

        book = Book.query.get_or_404(book_id)
        book.title = data.get('title')
        book.author = data.get('author')

        db.session.add(book)
        db.session.commit()
        return {'success': True}

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return {'success': True}


class BooksResource(Resource):
    def get(self):
        """
        Используем постраничный вывод с помощью параметра запроса page
        https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/pagination/
        """
        page = db.paginate(db.select(Book).order_by(Book.title))
        return [b.to_dict() for b in page]

    def post(self):
        data = request.get_json()

        # TODO: валидация данных

        new_book = Book(title=data['title'], author=data['author'])

        db.session.add(new_book)
        db.session.commit()
        return {'success': True}
