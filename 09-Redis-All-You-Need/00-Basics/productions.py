from fastapi import FastAPI
import redis
import time
import requests
import json

app = FastAPI()

# Connect to Redis (running in Docker)
cache = redis.Redis(host="localhost", port=6379, db=0)

def get_data_from_external_api():
    """Simulate slow API (or DB) call"""
    time.sleep(2)  # simulate 2s delay
    return {"data": "This is the original data from slow source."}

@app.get("/data")
def get_data():
    cache_key = "api:data"

    # 1️⃣ Try to get data from cache
    cached_value = cache.get(cache_key)
    if cached_value:
        print("⚡ Cache hit")
        return json.loads(cached_value)

    print("🐢 Cache miss — fetching from slow source...")
    data = get_data_from_external_api()

    # 2️⃣ Store in Redis cache for 10 seconds
    cache.setex(cache_key, 10, json.dumps(data))

    return data
