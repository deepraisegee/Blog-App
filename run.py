from flask_migrate import Migrate
from config import create_app, db

app = create_app()
migrate = Migrate(app, db)
