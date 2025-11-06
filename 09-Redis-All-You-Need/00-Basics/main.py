from fastapi import FastAPI
import redis

app = FastAPI()

# Connect to Redis (your container)
r = redis.Redis(host="localhost", port=6379, db=0)

@app.get("/")
def read_root():
    return {"message": "Redis + FastAPI test running"}

@app.post("/set/{key}/{value}")
def set_value(key: str, value: str):
    r.set(key, value)
    return {"status": "success", "key": key, "value": value}

@app.get("/get/{key}")
def get_value(key: str):
    value = r.get(key)
    if value:
        return {"key": key, "value": value.decode("utf-8")}
    return {"error": "Key not found"}
