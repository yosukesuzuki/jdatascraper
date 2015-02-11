# -*- coding: utf-8 -*-
from kay.routing import (
    ViewGroup, Rule
)

view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='scraper.views.index'),
        Rule('/gameid', endpoint='get_and_save_game_id', view='scraper.views.get_and_save_game_id'),
    )
]
