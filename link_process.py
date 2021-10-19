import praw
from praw.exceptions import RedditAPIException, InvalidURL
from sentiment import cal_polarity
import credential as cr


# Log In to Reddit: 
reddit = praw.Reddit(client_id = cr.CLIENT_ID, client_secret = cr.SECRET, user_agent = cr.USER_AGENT)

def valid_post(post_link: str):
    try:
        res = reddit.submission(url = post_link)
    except Exception as e:
        return False
    return True
    
def extract_features(post_link: str):
    post = reddit.submission(url = post_link)
    features = [post.num_comments, cal_polarity(post.title), cal_polarity(post.selftext)]
    return features
