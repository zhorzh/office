from flask import jsonify
from core.services.postgres import postgres
from identity import blueprint
from identity.models.user import User


@blueprint.route('/user/<int:id>', methods=['DELETE'])
def delete(id):
    # find user if exists
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify(error='User not found'), 404

    # delete user
    postgres.session.delete(user)
    postgres.session.commit()

    return jsonify(user=user.serialize()), 200
