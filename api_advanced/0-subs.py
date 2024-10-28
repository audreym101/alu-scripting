import requests

def number_of_subscribers(subreddit):
    # Define the API URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set up custom headers to avoid Too Many Requests error
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0 (by /u/yourusername)"}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code is 200, indicating success
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers
            return data["data"]["subscribers"]
        else:
            # If the status code isn't 200, return 0
            return 0
    except Exception:
        # If an error occurs (e.g., connection error), return 0
        return 0

