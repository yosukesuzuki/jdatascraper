# -*- coding: utf-8 -*-
from kay.routing import (
    ViewGroup, Rule
)

view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='scraper.views.index'),
        Rule('/gameid', endpoint='get_and_save_game_id', view='scraper.views.get_and_save_game_id'),
        Rule('/gameresult', endpoint='get_and_save_game_result', view='scraper.views.get_and_save_game_result'),
        Rule('/gamestat', endpoint='set_game_stats', view='scraper.views.set_game_stats'),
        Rule('/alljson', endpoint='all_json', view='scraper.views.all_json'),
        Rule('/allcsv', endpoint='all_csv', view='scraper.views.all_csv'),
    )
]
