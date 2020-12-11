import json
import xml.etree.ElementTree as ET

def get_all_news(open_file, type_file):
    all_news = ''

    if type_file == 'json':

        with open(open_file) as f:
            json_data = json.load(f)

        news_list = json_data['rss']['channel']['items']

        for news in news_list:
            all_news += ' ' + news['description'].lower()

    elif type_file == 'xml':
        parser = ET.XMLParser(encoding='UTF-8')
        tree = ET.parse(open_file, parser)
        root = tree.getroot()

        news_list = root.findall('channel/item/description')

        for news in news_list:
            all_news += ' ' + news.text.lower()

    return(all_news)

def get_word_dict(open_file, type_file):

    word_dict = {}
    all_news = get_all_news(open_file, type_file)

    for word in sorted(all_news.split(' ')):
        if len(word) >= 6:
            count_word = all_news.count(word)
            word_dict[word] = count_word

    return(word_dict)

def get_top(type_file, open_file, top_count):
    list_word_dict = list(get_word_dict(open_file, type_file).items())
    list_word_dict.sort(key=lambda i: i[1])

    count = -1

    while count != -top_count - 1:
        print(list_word_dict[count])
        count -= 1

get_top('json', 'files/newsafr.json', 10)
print('======================')
get_top('xml', 'files/newsafr.xml', 10)