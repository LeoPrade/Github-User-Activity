# GitHub Activity CLI

A simple command line interface (CLI) to fetch and display the recent activity of a GitHub user directly in your terminal.

## Features

- Fetch recent public activity of any GitHub user
- Displays grouped events (e.g. multiple pushes to the same repository are combined)
- Graceful error handling for invalid usernames or connection issues

## Requirements

- Python 3.x
- No external libraries required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/github-activity.git
cd github-activity
```

2. Make sure Python 3 is installed:
```bash
python --version
```

## Usage

Run the script from the command line with a GitHub username as argument:

```bash
python main.py <username>
```

**Example:**
```bash
python main.py torvalds
```

**Output:**
```
Pushed 3 commits to torvalds/linux
Starred torvalds/linux
Opened a new issue on torvalds/linux
...
```

## Error Handling

- If no username is provided, the program will display a usage hint
- If the username is invalid or does not exist, the program will display an error message and exit
- Network errors are caught and handled gracefully

## Supported Event Types

| Event | Output |
|-------|--------|
| PushEvent | Pushed N commits to ... |
| IssuesEvent | Created new issue on ... |
| IssueCommentEvent | Commented on ... |
| WatchEvent | Starred ... |
| ForkEvent | Forked ... |
| CreateEvent | Created event as ... |
| DeleteEvent | Deleted ... |
| PullRequestEvent | Created pull request ... |
| PublicEvent | Published ... |

## License

This project is open source and available under the [MIT License](LICENSE).
