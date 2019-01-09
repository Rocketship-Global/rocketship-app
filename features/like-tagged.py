from instapy import InstaPy
from instapy.util import smart_run
from config import USERNAME, PASSWORD, USER1, USER2

# get a session!
session = InstaPy(username=USERNAME, password=PASSWORD)

# let's go! :>
with smart_run(session):
    # settings
    # session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.set_relationship_bounds (enabled=False,
                                       max_followers=999999,
                                       max_following=999999,
                                       min_followers=5,
                                       min_following=5)

    session.set_do_follow(enabled=False, percentage=50)
    session.set_comments(["Love it!", "Classy!"])
    session.set_do_comment(enabled=True, percentage=100)
    session.set_do_like(True, percentage=100)
    session.interact_by_users_tagged_posts([USER1], amount=2, randomize=False, media='Photo')