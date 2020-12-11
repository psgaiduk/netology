import json
import hashlib

def get_hash(file):
    with open(file) as f:
        json_data = json.load(f)
    start = 0
    end = len(json_data)
    while start< end:
        yield hashlib.md5(json_data[start].encode()).hexdigest()
        start += 1

for item in get_hash('count.json'):
    print(item)