from app.models.like import Like
from app.models import db

def init_likes(likesList):
    for item in likesList:
        author_id= item['author_id']
        post_id= item['post_id']

        like = Like(liked_by_id=author_id, post_id=post_id)
        # like.save()
        db.session.add(like)
    db.session.commit()



likesList = [
    {
        "author_id": 1,
        "post_id": 1
    },
    {
        "author_id": 2,
        "post_id": 1
    },
    {
        "author_id": 4,
        "post_id": 2
    },
    {
        "author_id": 5,
        "post_id": 2
    },
    {
        "author_id": 3,
        "post_id": 2
    },
] 