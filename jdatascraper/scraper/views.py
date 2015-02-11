# -*- coding: utf-8 -*-

from google.appengine.ext import db

from kay.utils import render_to_response, render_json_response

from core.models import GameId
from scraper.scrap import get_game_id


def save_game_id(game_ids):
    game_id_objects = []
    for game_id in game_ids:
        game_id_objects.append(GameId(key_name=game_id, game_id=game_id))
    db.put(game_id_objects)


def index(request):
    return render_to_response('scraper/index.html', {'message': 'Hello'})


def get_and_save_game_id(request):
    save_game_id(get_game_id(2014))
    return render_json_response({'status': 'done'})
