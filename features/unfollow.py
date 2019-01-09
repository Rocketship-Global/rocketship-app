from instapy import InstaPy
from instapy.util import smart_run
from config import USERNAME, PASSWORD, USER1, USER2

# get a session!
session = InstaPy(username=USERNAME, password=PASSWORD)

# let's go! :>
with smart_run(session):
    session.set_quota_supervisor(enabled=True, 
                              sleep_after=["unfollows"], 
                              sleepyhead=True, 
                              stochastic_flow=True, 
                              notify_me=True,
                              peak_unfollows=(90, 900))

    session.set_skip_users(skip_private=False)
    #popeye_followers = session.grab_followers(username=USERNAME, amount="full", live_match=True, store_locally=True)

    session.unfollow_users(amount=200, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=86400, sleep_delay=60) # people that havent followed back
