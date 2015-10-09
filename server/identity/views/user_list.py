from flask import jsonify
from identity import blueprint
from identity.models.user import User


@blueprint.route('/user')
def list():
    # find all users
    users = User.query.all()
    users = [user.serialize() for user in users]

    return jsonify(users=users)
