import requests
import redis
import time

# Initialize Redis connection
redis_conn = redis.Redis()

def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a URL and cache it with expiration time
    """
    # Increment access count for the URL
    redis_conn.incr(f"count:{url}")

    # Check if the page content is cached
    cached_content = redis_conn.get(url)
    if cached_content:
        return cached_content.decode()

    # Retrieve HTML content of the URL
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text

        # Cache the content with expiration time of 10 seconds
        redis_conn.setex(url, 10, content)

        return content
    else:
        return f"Error: Unable to retrieve content from {url}"
