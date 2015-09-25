import ipdb
from core import postgres


def before_scenario(context, scenario):
    postgres.drop_all()
    postgres.create_all()


def after_scenario(context, scenario):
    postgres.drop_all()


def after_step(context, step):
    if step.status == "failed":
        ipdb.post_mortem(step.exc_traceback)
