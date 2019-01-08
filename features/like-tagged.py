"""
This template is written by @Tachenz

What does this quickstart script aim to do?
- Interact with user followers, liking 3 pictures, doing 1-2 comment - and 25% chance of follow (ratios which work the best for my account)

NOTES:
- This is used in combination with putting a 40 sec sleep delay after every like the script does. It runs 24/7 at rather slower speed, but without problems (so far).
"""


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
                                       max_followers=3000,
                                       max_following=900,
                                       min_followers=5,
                                       min_following=5)

    session.set_skip_users(skip_private=False)

    # auto like
    session.set_do_like(True, percentage=100)
    session.interact_by_users_tagged_posts(['teamninja'], amount=2, randomize=False)