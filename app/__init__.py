from flask import Flask

from app.api import BookResource, BooksResource, api
from app.graphql import graphql_explorer, graphql_server
from app.models import db


def create_app(config=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if config:
        app.config.from_mapping(config)

    db.init_app(app)
    api.init_app(app)

    api.add_resource(BooksResource, '/books/')
    api.add_resource(BookResource, '/book/<int:book_id>/')

    app.add_url_rule('/graphql/', view_func=graphql_explorer, methods=['GET'])
    app.add_url_rule('/graphql/', view_func=graphql_server, methods=['POST'])

    return app
