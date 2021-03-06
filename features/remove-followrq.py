from instapy import InstaPy
from instapy.util import smart_run
from config import USERNAME, PASSWORD, USER1

# get a session!
session = InstaPy(username=USERNAME, password=PASSWORD)

# let's go! :>
with smart_run(session):
    session.set_quota_supervisor(enabled = True, sleep_after = ["unfollows"], sleepyhead = True, stochastic_flow = True, notify_me = True, peak_unfollows = (90, 900))
    session.remove_follow_requests(amount=200, sleep_delay=60)
