import os
import slack
import sys

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

response = client.chat_postMessage(
    channel='#general',
    text=sys.argv[1])
assert response["ok"]
assert response["message"]["text"] == sys.argv[1]
