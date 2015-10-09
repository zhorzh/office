from flask import Blueprint

blueprint = Blueprint(name='identity', import_name=__name__)

from identity.views import user_create
from identity.views import user_read
from identity.views import user_update
from identity.views import user_delete
