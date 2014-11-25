import time
import praw

user_agent = ("Chocolate 1.0 by /u/beardgoggles")

r = praw.Reddit(user_agent=user_agent)

r.login()
already_done = []

prawWords = ['ganache', 'chocolate']
while True:
    subreddit = r.get_subreddit('Baking')
    


