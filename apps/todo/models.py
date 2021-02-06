import sqlalchemy
from apps.user.models import users_table

metadata = sqlalchemy.MetaData()

status_table = sqlalchemy.Table(
    'status',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(100))
)

todos_table = sqlalchemy.Table(
    'todos',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('text', sqlalchemy.String(250)),
    sqlalchemy.Column('status_id', sqlalchemy.ForeignKey(status_table.c.id)),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime()),
    sqlalchemy.Column('date_to', sqlalchemy.DateTime()),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey(users_table.c.id))
)