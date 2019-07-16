from xbmcswift2 import Plugin, xbmcgui
from resources.lib import moderaterebels

plugin = Plugin()

URL = "https://moderaterebels.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://assets.libsyn.com/secure/show/103689/moderate_rebels_podcast_medium.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://assets.libsyn.com/secure/show/103689/moderate_rebels_podcast_medium.jpg"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = moderaterebels.get_soup(URL)
    
    playable_podcast = moderaterebels.get_playable_podcast(soup)
    
    items = moderaterebels.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = moderaterebels.get_soup(URL)
    
    playable_podcast1 = moderaterebels.get_playable_podcast1(soup)
    
    items = moderaterebels.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
