from unittest import TestCase
from app import app
from models import db, User, Post

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_user'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):

    def setup(self):
        User.query.delete()
        Post.query.delete()
        user = User(first_name="TJ", last_name="Kruger", image_url="https://media.licdn.com/dms/image/D5603AQFKnzTslWwnRw/profile-displayphoto-shrink_800_800/0/1674581102672?e=2147483647&v=beta&t=icnOpXwA3QBALljqIeQvXQY3xl50EcfnEmJBUv6ac84")
        post = Post(title="First Post", content="This is my first post!", user_id=1)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TJ', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>TJ Kruger</h1>', html)

    def test_add_user(self):
        with app.test_client() as client:
            u = {"first_name": "Tyler", "last_name": "Ike", "image_url": "https://media.licdn.com/dms/image/C4D03AQFAf1bUmI06Lw/profile-displayphoto-shrink_800_800/0/1648479353472?e=2147483647&v=beta&t=zPo8dEo7X82eJfuB7vg7Cz16iQemsV3pBKcIlVqndvg"}
            resp = client.post("/users/new", data=u, follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Tyler Ike</h1>', html)

    def test_new_post(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}/posts/new")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Title: ', html)

    def test_show_post(self):
        with app.test_client() as client:
            resp = client.get(f"/posts/{self.post_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>First Post</h1>', html)

    def test_add_post(self):
        with app.test_client() as client:
            p = {"title":"Second Post", "content": "This is my second post!", "user_id": "1"}
            resp = client.post(f"/users/{self.user_id}/posts/new", data=p, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Second Post', html)
