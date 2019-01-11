from instapy import InstaPy
from instapy.util import smart_run
from config import USERNAME, PASSWORD, USER1


# get a session!
session = InstaPy(username=USERNAME, password=PASSWORD) # headless_browser=True


# let's go! :>
with smart_run(session):
    session.set_quota_supervisor(enabled = True, sleep_after = ["follows", "unfollows"], sleepyhead = True, stochastic_flow = True, notify_me = True, peak_follows = (90, 900), peak_unfollows = (90, 900))
    session.set_relationship_bounds(enabled = True, max_followers = 999999, max_following = 999999, min_followers = 5, min_following = 5)
    session.set_skip_users(skip_private=False, skip_no_profile_pic=True, skip_business=True)
    counter = 0
    while True:
        print(f"\n\n===================== LOOP: {counter} =====================\n\n")
        session.follow_likers ([USER1], photos_grab_amount = 2, follow_likers_per_photo = 450, randomize=False, sleep_delay=80, interact=False)
        session.unfollow_users(amount=900, allFollowing=True, style="FIFO", sleep_delay=80) # unfollow_after=86400
        counter += 1
        print(f"\n\n===================== END LOOP =====================\n\n")
        