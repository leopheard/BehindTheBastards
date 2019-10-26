from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/behindthebastards"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/22c36480-3778-11e8-806d-cfb84f1d0648/image/uploads_2F1547069138516-4edafwuejvc-14cc4c048140986ac2bacd6b0e0f022d_2FBehindTheBastards-Logo-iHR-FINAL-3000x3000.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/22c36480-3778-11e8-806d-cfb84f1d0648/image/uploads_2F1547069138516-4edafwuejvc-14cc4c048140986ac2bacd6b0e0f022d_2FBehindTheBastards-Logo-iHR-FINAL-3000x3000.jpg"},
    ]
    return items

@plugin.route('/episodes1/'
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
