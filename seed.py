from models import User, db, Post, Tag, PostTag
from app import app


db.drop_all()
db.create_all()

#PostTag.query.delete()
User.query.delete()
Post.query.delete()
Tag.query.delete()
print("Line 12")
Tom = User(first_name="Thomas", last_name="Kruger", image_url="https://media.licdn.com/dms/image/D5603AQFKnzTslWwnRw/profile-displayphoto-shrink_800_800/0/1674581102672?e=2147483647&v=beta&t=icnOpXwA3QBALljqIeQvXQY3xl50EcfnEmJBUv6ac84")
Tyler = User(first_name="Tyler", last_name="Ike", image_url="https://media.licdn.com/dms/image/C4D03AQFAf1bUmI06Lw/profile-displayphoto-shrink_800_800/0/1648479353472?e=2147483647&v=beta&t=zPo8dEo7X82eJfuB7vg7Cz16iQemsV3pBKcIlVqndvg")
Cam = User(first_name="Camden", last_name="Hartman", image_url="https://media.licdn.com/dms/image/C4E03AQEnDuxjoHnUyA/profile-displayphoto-shrink_800_800/0/1643673102277?e=2147483647&v=beta&t=a-5uK1NzZHktpNcnLZqdyGMoMe23lzgDUtOmPOgW1JM")

db.session.add(Tom)
db.session.add(Tyler)
db.session.add(Cam)

post = Post(title="First Post", content="I hate McDonalds", user_id=3)

db.session.add(post)

tag = Tag(name="First")
tag2 = Tag(name="Second")

db.session.add(tag)
db.session.add(tag2)

posttag = PostTag(post_id=1, tag_id=1)
posttag2 = PostTag(post_id=1, tag_id=2)

db.session.add(posttag)
db.session.add(posttag2)

db.session.commit()