# -*- coding: utf-8 -*-
from kay.routing import (
    ViewGroup, Rule
)

view_groups = [
    ViewGroup(
        Rule('/gamestats/<string:game_id>', endpoint='gamestats', view='main.views.gamestats'),
        Rule('/', endpoint='index', view='main.views.index'),
    )
]
