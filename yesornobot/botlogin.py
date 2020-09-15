import praw
import os

def bot_login():
    print ("Logging in..")
    try:
        r = praw.Reddit(username = os.environ["learnbotmaking"],
                password = os.environ["learnbotmaking"],
                client_id = os.environ["DKCBqL1Plj8F8A"],
                client_secret = os.environ["utsa-fyYdzgIqVjX-Pn4w3zvu08"],
                user_agent = "alita")
        print ("Logged in!")
    except:
        print ("Failed to log in!")
    return r