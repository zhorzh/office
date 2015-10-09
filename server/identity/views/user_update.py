from flask import request
from flask import jsonify
from core.services.postgres import postgres
from identity import blueprint
from identity.models.user import User


@blueprint.route('/user/<int:id>', methods=['PATCH'])
def update(id):
    # find user if exists
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify(error='User not found'), 404

    # update user
    try:
        user.email = request.get_json()['data']['email']
    except KeyError:
        pass

    try:
        user.set_password(request.get_json()['data']['password'])
    except KeyError:
        pass

    # save user to the database
    postgres.session.commit()

    return jsonify(user=user.serialize()), 200
