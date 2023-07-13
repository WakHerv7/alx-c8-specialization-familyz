from flask import Blueprint, jsonify, request
from app.models.comment import Comment

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify([comment.serialize() for comment in comments])

@comment_bp.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        return jsonify(comment.serialize())
    return jsonify({'error': 'Comment not found'}), 404

@comment_bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Content is required'}), 400

    comment = Comment(content=content)
    comment.save()
    return jsonify(comment.serialize()), 201

@comment_bp.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return jsonify({'error': 'Comment not found'}), 404

    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Content is required'}), 400

    comment.content = content
    comment.save()
    return jsonify(comment.serialize())

@comment_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return jsonify({'error': 'Comment not found'}), 404

    comment.delete()
    return jsonify({'message': 'Comment deleted'})
