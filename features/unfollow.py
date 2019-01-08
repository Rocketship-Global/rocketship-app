"""
This template is written by @Tachenz

What does this quickstart script aim to do?
- Interact with user followers, liking 3 pictures, doing 1-2 comment - and 25% chance of follow (ratios which work the best for my account)

NOTES:
- This is used in combination with putting a 40 sec sleep delay after every like the script does. It runs 24/7 at rather slower speed, but without problems (so far).
"""


from instapy import InstaPy
from instapy.util import smart_run
from config import USERNAME, PASSWORD, USER1, USER2, BLACKLIST



# get a session!
session = InstaPy(username=USERNAME, password=PASSWORD)
#blacklist = BLACKLIST


# let's go! :>
with smart_run(session):
    # settings
    # session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    # session.set_relationship_bounds (enabled=True,
    #                                    max_followers=3000,
    #                                    max_following=900,
    #                                    min_followers=5,
    #                                    min_following=5)
    # session.set_simulation(enabled=False)
    # session.set_do_like(enabled=True, percentage=100)
    # session.set_ignore_users([])
    # session.set_do_comment(enabled=True, percentage=35)
    # session.set_do_follow(enabled=True, percentage=25, times=1)
    # session.set_comments([])
    # session.set_ignore_if_contains([])
    # session.set_action_delays(enabled=True, like=40)

    # so, we would unfollow those that have followed us back before unfollowing those that havent yet followed back

    session.set_skip_users(skip_private=False)
    

    # session.set_dont_include(blacklist)
    # only unfollow users that the bot has followed.
    session.unfollow_users(amount=200, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=86400, sleep_delay=60) # people that havent followed back
    #session.unfollow_users(amount=90, allFollowing=True, style="LIFO", sleep_delay=60)



    #session.unfollow_users(amount=300, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=86400, store_locally=True, sleep_delay=60) # all users