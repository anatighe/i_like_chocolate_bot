import time
import praw
import pprint

r = praw.Reddit("Chocolate 1.0 by /u/beardgoggles")

username = input("username: ")
password = input("Password: ")

r.login(username,password)

already_done = []

prawWords = ['chocolate', 'ganache']
while True:
    subreddit = r.get_subreddit('Baking')
    for submission in subreddit.get_hot(limit=20):
        op_text = submission.title.lower()
        has_praw = any(string in op_text for string in prawWords)
        if submission.id not in already_done and has_praw:
            submission.upvote()
            already_done.append(submission.id)
            pprint.pprint(submission.title)
            
    time.sleep(30)
    


