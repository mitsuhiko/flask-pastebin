from flask.ext.script import Manager
from pastebin import app, db


manager = Manager(app)


@manager.command
def initdb():
    """Creates all database tables."""
    db.create_all()


@manager.command
def dropdb():
    """Drops all database tables."""
    db.drop_all()


if __name__ == '__main__':
    manager.run()
