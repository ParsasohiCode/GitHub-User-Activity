import requests
import sys

def get_latest_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code} - {response.reason}")
        return

    data = response.json()
    
    if not data:
        print("No recent activity found.")
        return

    print(f"\nLatest public activities of '{username}':\n" + "=" * 40)
    
    for event in data:
        event_type = event['type']
        repo_name = event['repo']['name']
        created_at = event['created_at']
        print(f"Event Type : {event_type}")
        print(f"Repository : {repo_name}")
        print(f"Time       : {created_at}")
        print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <github_username>")
    else:
        get_latest_activity(sys.argv[1])
