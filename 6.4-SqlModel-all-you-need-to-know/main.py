from app.models import User, Profile, BlogPost, Tag, PostTagLink
from app.db_utils import get_session
from sqlmodel import select


# with get_session() as session:
#     stmt = select(User).where(User.username == "john_doe")
#     user = session.exec(stmt).one()   # .one() will raise if none/multiple
#     print("User:", user.username, user.id, user.created_at)

#     # Access posts (lazy-loads when first referenced)
#     print("Posts count:", len(user.blog_posts))
#     for p in user.blog_posts:
#         print("-", p.id, p.title, p.published_at)


# from sqlalchemy.orm import selectinload

# with get_session() as session:
#     stmt = select(User).options(selectinload(User.blog_posts))
#     users = session.exec(stmt).all()
#     for u in users[:5]:
#         print(u.username, "->", len(u.blog_posts))


from datetime import datetime
from uuid import UUID

with get_session() as session:
    user = session.exec(select(User).where(User.username == "john_doe")).one()
    new_post = BlogPost(
        title="ORM Tricks I Use",
        content="Notes about SQLModel and relationships.",
        published_at=datetime.utcnow(),
        author=user  # set object; ORM will set user_id automatically
    )
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    print("Created post id:", new_post.id, "user_id:", new_post.user_id)
