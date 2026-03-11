import urllib.request
import json
import sys
import urllib.error
from collections import Counter


if len(sys.argv) < 2:
    print("Usage: python github-activity.py <username>")
    sys.exit(1)

username: str = sys.argv[1]

url: str = f"https://api.github.com/users/{username}/events"

request = urllib.request.Request(url, headers={"User-Agent": "my-app"})

try:
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read())
except (urllib.error.HTTPError, urllib.error.URLError) as e: 
    print("Invalid username")
    sys.exit(1)

events: dict[str, str] = {
    "PushEvent" : "Pushed ",
    "IssuesEvent" : "Created new issue on ",
    "IssueCommentEvent" : "Commented on ",
    "WatchEvent" : "Starred ",
    "ForkEvent" : "Forked ",
    "CreateEvent" : "Created an event as ",
    "DeleteEvent" : "Deleted ",
    "PullRequestEvent" : "Created a pull request on ",
    "PublicEvent" : "Published ",
    }

counter: Counter = Counter((d['type'], d['repo']['name']) for d in data[:8])

for (type, reponame), count in counter.items():
    if type == "PushEvent" and count > 1:
        event_commands: str = f"Pushed {count} commits to {reponame}"
    else:
        event_commands: str = f"{events.get(type, 'No event found for ')}{reponame}"
    print(event_commands)