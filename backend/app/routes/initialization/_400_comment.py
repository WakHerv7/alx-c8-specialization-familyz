from app.models.comment import Comment
from app.models import db

def init_comments(commentsList):
    for item in commentsList:
        content = item['content']
        author_id= item['author_id']
        post_id= item['post_id']

        comment = Comment(content=content, author_id=author_id, post_id=post_id)
        # comment.save()
        db.session.add(comment)
    db.session.commit()


commentsList = [
    {
        "content": "LOL",
        "author_id": 1,
        "post_id": 1
    },
    {
        "content": "I don't get it.",
        "author_id": 4,
        "post_id": 1
    },
    {
        "content": "Thank you dad.",
        "author_id": 4,
        "post_id": 2
    },
    {
        "content": "I don't think I need Personal Branding as a student.",
        "author_id": 5,
        "post_id": 2
    },
    {
        "content": "Trust me. You're gonna need it to find a job.",
        "author_id": 3,
        "post_id": 2
    },
] 