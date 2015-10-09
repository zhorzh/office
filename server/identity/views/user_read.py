from flask import jsonify
from identity import blueprint
from identity.models.user import User


@blueprint.route('/user/<int:id>')
def read(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify(error='User not found'), 404
    return jsonify(user=user.serialize())
