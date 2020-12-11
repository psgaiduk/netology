import requests


def create_ya_disk_folder(folder_name):
    with open('token') as file:
        token = file.read()
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': token}
    params = {'path': folder_name, 'overwrite': 'True'}

    resp = requests.put(url, headers=headers, params=params)
    print(resp)


folder_name = input('Введите имя папки: ')
create_ya_disk_folder(folder_name)
