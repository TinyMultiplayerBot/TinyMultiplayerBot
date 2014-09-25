from flask.ext.script import Manager

from tmb import app, db

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

if __name__ == '__main__':
    manager.run()
