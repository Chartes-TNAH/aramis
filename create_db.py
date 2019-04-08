from app.app import db, config_app

app = config_app("production")

with app.app_context():
    db.create_all()

