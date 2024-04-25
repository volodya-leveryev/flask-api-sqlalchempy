from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author}
