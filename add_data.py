from database import SessionLocal
from models import User, Post

db = SessionLocal()

# Добавление пользователей
users = [
    User(username="john_doe", email="john@example.com", password="secure123"),
    User(username="jane_doe", email="jane@example.com", password="strong456"),
]
db.add_all(users)
db.commit()

# Добавление постов
posts = [
    Post(title="First Post", content="This is the first post", user_id=1),
    Post(title="Second Post", content="This is the second post", user_id=2),
]
db.add_all(posts)
db.commit()
db.close()
print("Data added!")
