import requests

# class YaUploader:
#     def __init__(self, file_path: str):
#         self.file_path = file_path

#     def upload(self):
#         """Метод загружает файлы по списку file_list на яндекс диск"""
#         # Тут ваша логика
#         URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
#         headers = {'Content-Type': 'application/json', 'Authorization': 'AgAAAAABlo8fAADLW3oEtk-9ZkAEm96aREYHXKQ'}
#         resp = requests.get(URL,headers=headers)
#         resp_json = resp.json()
#         return(resp_json)


# if __name__ == '__main__':
#     uploader = YaUploader('c:\my_folder\file.txt')
#     result = uploader.upload()


filepath = 'text.txt'

URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {'Content-Type': 'application/json', 'Authorization': ''}
params = {'path': filepath, 'overwrite': 'True'}

resp = requests.get(URL,headers=headers,params=params)
resp_json = resp.json()

URL = resp_json['href']
# with open('test.txt', 'rb') as f:
#     print(f)
#     r = requests.put(URL,data={'file': 'text.txt'})
#     print(r)


with open(filepath, 'rb') as fh:
    mydata = fh.read()
    response = requests.put(URL, data=mydata, params={'file': filepath})
    print(response)