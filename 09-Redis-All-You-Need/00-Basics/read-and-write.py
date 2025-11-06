import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)

# Write test
start = time.time()
for i in range(100000):
    r.set(f"key{i}", f"value{i}")
end = time.time()
print(f"Write 100000 keys in: {end - start:.4f} seconds")

# Read test
start = time.time()
for i in range(100000):
    r.get(f"key{i}")
end = time.time()
print(f"Read 100000 keys in: {end - start:.4f} seconds")
