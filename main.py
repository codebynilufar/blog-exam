import json
from database import engine, LocalSession, Base
from models import User, Post, Comment

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def load_demo_data():
    db = LocalSession()
    with open("demo_data.json", "r") as f:
        data = json.load(f)

    # Users larni kriting

    for u in data["users"]:
        user = User(username=u["username"], email=u["email"])
        db.add(user)

    # Posts larni kriting
    for p in data["posts"]:
        post = Post(title=p["title"], body=p["body"], user_id=p["user_id"])
        db.add(post)

    # Comments larni kriting
    for c in data["comments"]:
        comment = Comment(text=c["text"], user_id=c["user_id"], post_id=c["post_id"])
        db.add(comment)
    db.commit()

    db.close()

if __name__ == "__main__":
    init_db()
    load_demo_data()
    print("✅ Database initialized and demo data loaded!")
