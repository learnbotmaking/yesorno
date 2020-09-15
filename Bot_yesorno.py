import praw
from random import randrange
import re
import time

reddit = praw.Reddit(user_agent='learnbotmaking version:1.0.0.0 u/learnbotmaking',
                  client_id='DKCBqL1Plj8F8A',
                  client_secret='utsa-fyYdzgIqVjX-Pn4w3zvu08',
                  username='learnbotmaking',
                  password='learnbotmaking')

def getResponse():
    number = randrange(1, 1000000)
    if number == 1000000:
        return "B&"
    elif number == 999999:
        return "PLATINUM AWARD"
    elif number == 999998:
        return "GOLD AWARD"
    elif number == 999997:
        return "SILVER AWARD"
    else:
        if number % 2 == 0:
            return "Yes"
        else:
            return "No"

subreddit = reddit.subreddit('yesorno')

for submission in subreddit.stream.submissions():
    if re.search("!YesOrNo", submission.title, re.IGNORECASE):
        response = getResponse()
        submission.reply(response)
        
        if response == "B&":
          # Ban the post author.
          subreddit.banned.add(submission.author.name, ban_reason="You got 'B&' as a response.")
        elif response == "PLATINUM AWARD":
          # Give a platinum award to the post.
          submission.gild("gid_3")
        elif response == "GOLD AWARD":
          # Give a gold award to the post.
          submission.gild("gid_2")
        elif response == "SILVER AWARD":
          # Give a silver award to the post.
          submission.gild("gid_1")
          
        time.sleep(10)
