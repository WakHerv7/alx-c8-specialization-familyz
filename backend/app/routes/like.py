[09:43, 7/13/2023] +234 811 189 7796: from flask import Blueprint, jsonify, request
from app.models.like import Like

like_bp = Blueprint('like_bp', _name_)

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
[09:43, 7/13/2023] +234 811 189 7796: from flask import Blueprint, jsonify, request
from app.models.comment import Comment

comment_bp = Blueprint('comment_bp', _name_)

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
