from core import app
from core.services.postgres import postgres
from identity.models.user import User


@app.cli.command()
def reset_postgres():
    """Reset postgres database"""
    postgres.drop_all()
    postgres.create_all()
