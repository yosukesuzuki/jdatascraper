# -*- coding: utf-8 -*-
import re
from google.appengine.api import urlfetch

from pyquery import PyQuery as pq


def get_game_id(year):
    game_id_pattern = re.compile(ur'(\d+)$')
    game_ids = []
    for i in range(3, 13):
        url = 'https://data.j-league.or.jp/SFMS01/search?' \
              + 'competition_years=' + str(year) \
              + '&competition_frame_ids=1&competition_frame_ids=&' \
              + 'section_months=' + str(i)
        html_string = unicode(urlfetch.fetch(url=url, deadline=60).content,'utf-8')
        query = pq(html_string)
        for e in query.find('td.al-c>a'):
            game_id = game_id_pattern.search(e.attrib['href']).group(1)
            game_ids.append(game_id)
    return game_ids
