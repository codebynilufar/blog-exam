from database import SessionLocal
import crud

db = SessionLocal()

user = crud.create_user(db, "test_user", "test@example.com")
print("User qo‘shildi:", user.username, user.email)

post = crud.create_post(db, user.id, "My First Post", "Hello, world!")
print("Post qo‘shildi:", post.title)

comment = crud.create_comment(db, user.id, post.id, "Nice post!")
print("Comment qo‘shildi:", comment.text)

print("User postlari:", [p.title for p in crud.get_user_posts(db, user.id)])
print("Commentlar soni:", crud.get_post_comment_count(db, post.id))

updated_post = crud.update_post(db, post.id, "Updated Post", "New content")
print("Post yangilandi:", updated_post.title, updated_post.body)

print("Latest posts:", [p.title for p in crud.get_latest_posts(db)])
print("Search results:", [p.title for p in crud.search_posts_by_title(db, 'Updated')])
print("Pagination:", [p.title for p in crud.paginate_posts(db, page=1, per_page=2)])

crud.delete_post(db, post.id)
print("Post o‘chirildi!")
print("User postlari (o‘chirgandan keyin):", [p.title for p in crud.get_user_posts(db, user.id)])

db.close()
