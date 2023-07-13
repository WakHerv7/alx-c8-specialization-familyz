from flask import Blueprint, jsonify, request
from app.models.family import Family

family_bp = Blueprint('family_bp', __name__)

@family_bp.route('/families', methods=['GET'])
def get_families():
    families = Family.query.all()
    return jsonify([family.serialize() for family in families])

@family_bp.route('/families/<int:family_id>', methods=['GET'])
def get_family(family_id):
    family = Family.query.get(family_id)
    if family:
        return jsonify(family.serialize())
    return jsonify({'error': 'Family not found'}), 404

@family_bp.route('/families', methods=['POST'])
def create_family():
    data = request.get_json()
    name = data.get('name')
    members = data.get('members')

    if not name or not members:
        return jsonify({'error': 'Name and members are required'}), 400

    family = Family(name=name, members=members)
    family.save()
    return jsonify(family.serialize()), 201

@family_bp.route('/families/<int:family_id>', methods=['PUT'])
def update_family(family_id):
    family = Family.query.get(family_id)
    if not family:
        return jsonify({'error': 'Family not found'}), 404

    data = request.get_json()
    name = data.get('name')
    members = data.get('members')

    if not name or not members:
        return jsonify({'error': 'Name and members are required'}), 400

    family.name = name
    family.members = members
    family.save()
    return jsonify(family.serialize())

@family_bp.route('/families/<int:family_id>', methods=['DELETE'])
def delete_family(family_id):
    family = Family.query.get(family_id)
    if not family:
        return jsonify({'error': 'Family not found'}), 404

    family.delete()
    return jsonify({'message': 'Family deleted'})

