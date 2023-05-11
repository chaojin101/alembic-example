from app.database import Base

import sqlalchemy as sa

class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    username = sa.Column(sa.String, index=True)
