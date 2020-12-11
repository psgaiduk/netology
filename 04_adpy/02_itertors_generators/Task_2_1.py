import json

class Myrange:
    def __init__(self, file):
        with open(file) as f:
            json_data = json.load(f)
        self.json_data = json_data
        self.start = 0
        self.end = len(json_data)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.json_data[self.start]

# with open('countries.json') as f:
#     json_data = json.load(f)

# print(len(json_data))

for item in Myrange('countries.json'):
    print(f"{item['name']['common']} - wikipedia.com/{(item['name']['common']).replace(' ', '-')}.html")