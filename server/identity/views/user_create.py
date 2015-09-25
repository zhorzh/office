from flask import request
from flask import jsonify
from core.services.postgres import postgres
from identity import blueprint
from identity.models.user import User


@blueprint.route('/user', methods=['POST'])
def create():
    # get data from request
    try:
        email = request.get_json()['data']['email']
        password = request.get_json()['data']['password']
    except KeyError:
        return jsonify(error='Invalid email or password'), 400

    # create user if not exists
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify(error='User with such email is already exists'), 409
    user = User(email, password)

    # save user to the database
    postgres.session.add(user)
    postgres.session.commit()

    return jsonify(user=user.serialize()), 200
