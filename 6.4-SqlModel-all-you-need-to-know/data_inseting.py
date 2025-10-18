# main.py
import json
from sqlmodel import select
from app.models import User, Profile, BlogPost, Tag, PostTagLink
from app.db_utils import get_session


def insert_user_data(data_file: str, username: str):
    """Insert only the specified user's data (e.g., Al Amin) into the DB."""
    # Load JSON
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    users = data.get("users", [])
    user_data = next((u for u in users if u["username"] == username), None)
    if not user_data:
        print(f"❌ User '{username}' not found in JSON.")
        return

    with get_session() as session:
        # 1️⃣ Check if user already exists
        existing_user = session.exec(
            select(User).where(User.username == user_data["username"])
        ).first()
        if existing_user:
            print(f"⚠️ User '{username}' already exists. Skipping insert.")
            return

        # 2️⃣ Create User
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            full_name=user_data["full_name"],
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"✅ User '{user.username}' inserted with id={user.id}")

        # 3️⃣ Create Profile (1:1)
        profile_data = user_data.get("profile")
        if profile_data:
            profile = Profile(
                bio=profile_data.get("bio"),
                avatar_url=profile_data.get("avatar_url"),
                user=user,  # ORM link
            )
            session.add(profile)
            session.commit()
            print(f"✅ Profile created for user '{user.username}'")

        # 4️⃣ Create Blog Posts and Tags (1:M and M:M)
        for post_data in user_data.get("blog_posts", []):
            post = BlogPost(
                title=post_data["title"],
                content=post_data["content"],
                published_at=post_data["published_at"],
                author=user,
            )
            session.add(post)
            session.commit()
            session.refresh(post)
            print(f"📝 Post '{post.title}' inserted")

            # Handle tags for this post
            for tag_name in post_data.get("tags", []):
                # Check if tag already exists
                tag = session.exec(select(Tag).where(Tag.name == tag_name)).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    session.add(tag)
                    session.commit()
                    session.refresh(tag)
                    print(f"🏷️  New tag created: {tag.name}")

                # Link post <-> tag
                link_exists = session.exec(
                    select(PostTagLink).where(
                        PostTagLink.post_id == post.id, PostTagLink.tag_id == tag.id
                    )
                ).first()
                if not link_exists:
                    link = PostTagLink(post_id=post.id, tag_id=tag.id)
                    session.add(link)
                    session.commit()
                    print(f"🔗 Linked post '{post.title}' ↔ tag '{tag.name}'")

        print(f"\n🎉 All data for '{user.username}' inserted successfully!\n")


if __name__ == "__main__":
    insert_user_data("db_data.json", "Al Amin")
