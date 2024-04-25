"""
Статья о GraphQL
https://habr.com/ru/articles/765064/

Используем пример из Ariadne:
https://ariadnegraphql.org/docs/flask-integration
"""

from ariadne import QueryType, graphql_sync, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL
from flask import jsonify, request

from app.models import Book, db

type_defs = """
    type Book {
        id: Int
        title: String
        author: String
    }

    type Query {
        books: [Book]
        book(id: Int!): Book!
    },
"""

query = QueryType()


@query.field("books")
def resolve_books(_obj, _info):
    query = db.select(Book).order_by(Book.title)
    books = db.session.execute(query).scalars()
    return [b.to_dict() for b in books]


@query.field("book")
def resolve_books(_obj, _info, id):
    book = Book.query.get_or_404(id)
    return book.to_dict()


def graphql_explorer():
    return explorer_html, 200


def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema, data,
        context_value={"request": request},
        # debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


schema = make_executable_schema(type_defs, query)

explorer_html = ExplorerGraphiQL().html(None)
