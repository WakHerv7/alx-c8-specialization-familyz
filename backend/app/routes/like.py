from flask import Blueprint, jsonify, request
from app.models.like import Like

like_bp = Blueprint('like_bp', __name__)

@like_bp.route('/likes', methods=['GET'])
def get_likes():
    likes = Like.query.all()
    return jsonify([like.serialize() for like in likes])

@like_bp.route('/likes/<int:like_id>', methods=['GET'])
def get_like(like_id):
    like = Like.query.get(like_id)
    if like:
        return jsonify(like.serialize())
    return jsonify({'error': 'Like not found'}), 404

@like_bp.route('/likes', methods=['POST'])
def create_like():
    data = request.get_json()
    user_id = data.get('user_id')
    post_id = data.get('post_id')

    if not user_id or not post_id:
        return jsonify({'error': 'User ID and Post ID are required'}), 400

    like = Like(user_id=user_id, post_id=post_id)
    like.save()
    return jsonify(like.serialize()), 201

@like_bp.route('/likes/<int:like_id>', methods=['DELETE'])
def delete_like(like_id):
    like = Like.query.get(like_id)
    if not like:
        return jsonify({'error': 'Like not found'}), 404

    like.delete()
    return jsonify({'message': 'Like deleted'})
