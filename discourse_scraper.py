import requests
import time
import json
from datetime import datetime

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY = "tools-in-data-science"
START_DATE = "2025-01-01"
END_DATE = "2025-04-14"

def get_all_topics():
    page = 0
    all_topics = []
    
    while True:
        url = f"{BASE_URL}/c/{CATEGORY}.json?page={page}"
        print(f"Fetching page {page}...")
        response = requests.get(url)
        
        if response.status_code != 200:
            break
        
        data = response.json()
        topics = data.get("topic_list", {}).get("topics", [])
        
        if not topics:
            break
        
        for topic in topics:
            created = topic.get("created_at", "")
            if START_DATE <= created[:10] <= END_DATE:
                all_topics.append(topic)
        
        page += 1
        time.sleep(1)  # To respect rate limit

    return all_topics

def save_to_file(topics, filename="discourse_topics.json"):
    with open(filename, "w") as f:
        json.dump(topics, f, indent=2)
    print(f"Saved {len(topics)} topics to {filename}")

if __name__ == "__main__":
    topics = get_all_topics()
    save_to_file(topics)
