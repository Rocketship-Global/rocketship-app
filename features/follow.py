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
    session.set_relationship_bounds (enabled=True,
                                       max_followers=3000,
                                       max_following=900,
                                       min_followers=5,
                                       min_following=5)
    
    # manage private users
    session.set_skip_users(skip_private=False, skip_no_profile_pic=True, skip_business=True)
    # follow
    session.follow_likers ([USER1, USER2], photos_grab_amount = 2, follow_likers_per_photo = 50, randomize=False, sleep_delay=60, interact=False)