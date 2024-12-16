from database import SessionLocal
from models import User, Post

db = SessionLocal()

# Все пользователи
users = db.query(User).all()
print("Users:", users)

# Все посты с авторами
posts = db.query(Post).all()
for post in posts:
    print(f"Post: {post.title}, Author: {post.user.username}")

# Посты конкретного пользователя
user_posts = db.query(Post).filter(Post.user_id == 1).all()
print("Posts by user 1:", user_posts)

db.close()
