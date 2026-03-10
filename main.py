import urllib.request
import json
import sys
import urllib.error


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
    "PushEvent" : "Pushed to ",
    "IssuesEvent" : "Created new issue on ",
    "IssueCommentEvent" : "Commented on ",
    "WatchEvent" : "Starred ",
    "ForkEvent" : "Forked ",
    "CreateEvent" : "Created event as ",
    "DeleteEvent" : "Deleted ",
    "PullRequestEvent" : "Created pull request ",
    "PublicEvent" : "Published ",
    }

for d in data[:4]:
    print(f"{events.get(d['type'], 'No event found for ')}{d['repo']['name']}")

print(data[0]["payload"])