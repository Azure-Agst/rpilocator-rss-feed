import requests
import feedparser
import time
import os

# Feed URL
# FEED_URL = 'https://pilocator.com/feed/'
FEED_URL = os.getenv('FEED_URL')
if not FEED_URL:
    raise Exception('FEED_URL not set!')

# After creating your Pushover account, register your application
# User Key
PUSHOVER_KEY = os.getenv('PUSHOVER_KEY')
if not PUSHOVER_KEY:
    raise Exception('PUSHOVER_KEY not set!')

# Application Key
PUSHOVER_API_KEY = os.getenv('PUSHOVER_API_KEY')
if not PUSHOVER_API_KEY:
    raise Exception('PUSHOVER_API_KEY not set!')

# Customize the message title
MESSAGE_TITLE = 'xlocator Stock Alert'

# User Agent
USER_AGENT = 'xlocator feed alert'

# Create the message body
def formatMessage(entry):

    messageData = 'token='+PUSHOVER_API_KEY+'&user='+PUSHOVER_KEY+'&title='+MESSAGE_TITLE

    message = messageData+'&message='+entry.title+'&url='+entry.link

    return message

# Send the push/message to all devices connected to Pushbullet
def sendMessage(message):
    
    try:
        req = requests.post(url='https://api.pushover.net/1/messages.json', data=message, timeout=20)
    except requests.exceptions.Timeout:
        print('Request Timeout')
        pass
    except requests.exceptions.TooManyRedirects:
        print('Too many requests')
        pass
    except requests.exceptions.RequestException as e:
        print(e)
        pass

# Set control to blank list
control = []

# Fetch the feed
f = feedparser.parse(FEED_URL, agent=USER_AGENT)

# If there are entries in the feed, add entry guid to the control variable
if f.entries:
    for entries in f.entries:
        control.append(entries.id)

#Only wait 30 seconds after initial run.
time.sleep(30)

while True:
    # Fetch the feed again, and again, and again...
    f = feedparser.parse(FEED_URL, agent=USER_AGENT)

    # Compare feed entries to control list.
    # If there are new entries, send a message/push
    # and add the new entry to control variable
    for entries in f.entries:
        if entries.id not in control:

            message = formatMessage(entries)

            sendMessage(message)

            # Add entry guid to the control variable
            control.append(entries.id)

    time.sleep(59)



