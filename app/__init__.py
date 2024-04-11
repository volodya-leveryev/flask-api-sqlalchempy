from flask import Flask
from flask_graphql import GraphQLView

from app.api import BookResource, BooksResource, api
from app.models import db, schema


def create_app(config=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if config:
        app.config.from_mapping(config)

    api.init_app(app)
    db.init_app(app)

    api.add_resource(BooksResource, '/books/')
    api.add_resource(BookResource, '/book/<int:book_id>/')

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
        'graphql', schema=schema, graphiql=True,
    ))

    return app
