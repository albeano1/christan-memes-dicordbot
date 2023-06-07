import os
import praw
from urllib.parse import urlparse
import random

def create_reddit_client():
    client = praw.Reddit(
        client_id="TOKEN",
        client_secret="SECRET",
        user_agent="AGENT",
    )
    return client

def get_images_info(client, subreddit_name, limit):
    hot_memes = client.subreddit(subreddit_name).hot(limit=limit)
    images_info = []
    for post in hot_memes:
        if post.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images_info.append(post.url)
    return images_info

def get_random_meme_url():
    subreddit_name = "christianmemes"  # Replace with your desired subreddit name
    limit = 30  # The number of posts to fetch from the subreddit
    client = create_reddit_client()
    images_info = get_images_info(client, subreddit_name, limit)

    if images_info:
        random.shuffle(images_info)  # Shuffle the list of images randomly

        # Check if the history is empty or if all images have been shown
        if not get_random_meme_url.history or len(get_random_meme_url.history) == len(images_info):
            get_random_meme_url.history = []

        # Get the next image URL from the shuffled list that is not in history
        for image_url in images_info:
            if image_url not in get_random_meme_url.history:
                get_random_meme_url.history.append(image_url)
                return image_url

    return "Sorry, no images found."

# Store the history of fetched image URLs
get_random_meme_url.history = []

if __name__ == "__main__":
    # Install a compatible version of urllib3
    os.system("pip install urllib3==1.26.6")
