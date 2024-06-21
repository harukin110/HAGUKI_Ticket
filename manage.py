from flask_script import Manager
from flask_app import app

from flask_app.scripts.db import InitDB,DropDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.add_command('drop_db', DropDB())
    manager.run()
