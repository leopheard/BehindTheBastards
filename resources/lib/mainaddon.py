import requests
import re
from bs4 import BeautifulSoup

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item', limit=16):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://images.megaphone.fm/s514lBJDILp6AngqWH82ts0Y42JjWZc0dehAWt2vlz4/plain/s3://megaphone-prod/podcasts/22c36480-3778-11e8-806d-cfb84f1d0648/image/uploads_2F1547069138516-4edafwuejvc-14cc4c048140986ac2bacd6b0e0f022d_2FBehindTheBastards-Logo-iHR-FINAL-3000x3000.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://images.megaphone.fm/s514lBJDILp6AngqWH82ts0Y42JjWZc0dehAWt2vlz4/plain/s3://megaphone-prod/podcasts/22c36480-3778-11e8-806d-cfb84f1d0648/image/uploads_2F1547069138516-4edafwuejvc-14cc4c048140986ac2bacd6b0e0f022d_2FBehindTheBastards-Logo-iHR-FINAL-3000x3000.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
