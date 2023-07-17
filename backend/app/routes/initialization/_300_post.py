from app.models.post import Post
from app.models import db

def init_posts(postsList):
    for item in postsList:
        title = item['title']
        content = item['content']
        # picture = item['picture']
        author_id= item['author_id']

        post = Post(title=title, content=content, author_id=author_id)
        # post.save()
        db.session.add(post)
    db.session.commit()



postsList = [
    { 
        "title": "Nerd joke",
        "content": "Some prefer backend, some prefer frontend, but I always prefer weekend.",
        "author_id": 3
    },
    { 
        "title": "Personal Brand",
        "content": "Everyone wants to network with thought leaders and authoritative people, and that is why creating a personal brand is imperative to networking success.",
        "author_id": 1
    },
] 