# -*- coding: utf-8 -*-
import re
from google.appengine.api import urlfetch

from pyquery import PyQuery as pq

from scraper.zenhan import z2h


def get_game_id(year):
    game_id_pattern = re.compile(ur'(\d+)$')
    game_ids = []
    for i in range(3, 13):
        url = 'https://data.j-league.or.jp/SFMS01/search?' \
              + 'competition_years=' + str(year) \
              + '&competition_frame_ids=1&competition_frame_ids=2&' \
              + 'section_months=' + str(i)
        html_string = unicode(urlfetch.fetch(url=url, deadline=60).content, 'utf-8')
        query = pq(html_string)
        for e in query.find('td.al-c>a'):
            game_id = game_id_pattern.search(e.attrib['href']).group(1)
            game_ids.append(game_id)
    return game_ids


def scrap_game_data(html_string):
    query = pq(unicode(html_string))
    title_text = pq(query('p.t-txt')[0]).text()
    series_number_str = re.search(ur'第([１２３４５６７８９０0-9])節', title_text).group(1)
    # import pdb; pdb.set_trace()
    series_number = int(z2h(series_number_str, 2).encode("euc-jp"))
    return {
        'series_number': series_number,
    }
