from models import User, db
from app import app

db.drop_all()
db.create_all()

User.query.delete()

Tom = User(first_name="Thomas", last_name="Kruger", image_url="https://media.licdn.com/dms/image/D5603AQFKnzTslWwnRw/profile-displayphoto-shrink_800_800/0/1674581102672?e=2147483647&v=beta&t=icnOpXwA3QBALljqIeQvXQY3xl50EcfnEmJBUv6ac84")
Tyler = User(first_name="Tyler", last_name="Ike", image_user="https://media.licdn.com/dms/image/C4D03AQFAf1bUmI06Lw/profile-displayphoto-shrink_800_800/0/1648479353472?e=2147483647&v=beta&t=zPo8dEo7X82eJfuB7vg7Cz16iQemsV3pBKcIlVqndvg")
Cam = User(first_name="Camden", last_name="Hartman", image_user="https://media.licdn.com/dms/image/C4E03AQEnDuxjoHnUyA/profile-displayphoto-shrink_800_800/0/1643673102277?e=2147483647&v=beta&t=a-5uK1NzZHktpNcnLZqdyGMoMe23lzgDUtOmPOgW1JM")

db.session.add(Tom)
db.session.add(Tyler)
db.session.add(Cam)

db.session.commit()