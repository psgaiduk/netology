import requests

list_name = ['Hulk', 'Captain America', 'Thanos', 'Iron Man']
heroes_with_intelligence = {}
list_intelligence = []

for name in list_name:
    URL = 'https://superheroapi.com/api/2619421814940190/search/' + name.replace(' ', '%20')
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(URL,headers=headers)
    resp_json = resp.json()
    intelligence = resp_json['results'][0]['powerstats']['intelligence']
    name_hero = resp_json['results'][0]['name']
    # print(intelligence,name_hero)
    heroes_with_intelligence[name_hero] = intelligence
    list_intelligence.append(int(intelligence))

print(heroes_with_intelligence)
list_heroes_with_intelligence = list(heroes_with_intelligence.items())
list_heroes_with_intelligence.sort(key=lambda i: i[1])


for i in range(list_intelligence.count(max(list_intelligence))):
    print(f'Самый умный супер герой с интеллектом: {max(list_intelligence)}')
    print(list_heroes_with_intelligence[i][0])


