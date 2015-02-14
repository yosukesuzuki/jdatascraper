# -*- coding: utf-8 -*-

import logging
import datetime

from google.appengine.ext import db
from google.appengine.api import urlfetch

from kay.utils import render_to_response, render_json_response

from core.models import GameId, GameResult
from scraper.scrap import get_game_id, scrap_game_data


def save_game_id(game_ids):
    game_id_objects = []
    for game_id in game_ids:
        game_id_objects.append(GameId(key_name=game_id, game_id=game_id))
    db.put(game_id_objects)


def save_game_result(game_results):
    game_result_objects = []
    for game_result in game_results:
        # import pdb; pdb.set_trace()
        game_result_objects.append(GameResult(key_name=game_result['game_id'], **game_result))
    db.put(game_result_objects)


def index(request):
    return render_to_response('scraper/index.html', {'message': 'Hello'})


def get_and_save_game_id(request):
    save_game_id(get_game_id(2014))
    return render_json_response({'status': 'done'})


def get_and_save_game_result(request):
    game_ids = [entity.game_id for entity in GameId.all().fetch(1000)]
    game_results = []
    for game_id in game_ids:
        url = "https://data.j-league.or.jp/SFMS02/?match_card_id=" + game_id
        logging.info(url)
        html_string = unicode(urlfetch.fetch(url=url, deadline=60).content, 'utf-8')
        result = scrap_game_data(html_string)
        result['game_id'] = game_id
        game_results.append(result)
    save_game_result(game_results)
    return render_json_response({'status': 'done'})


def all_json(request):
    results = GameResult.all().order('game_start_at').fetch(1000)
    return_data = []
    for r in results:
        return_data.append({
            'series_number': r.series_number,
            'home_team': r.home_team,
            'away_team': r.away_team,
            'teams': r.teams,
            'home_director': r.home_director,
            'away_director': r.away_director,
            'home_score': r.home_score,
            'away_score': r.away_score,
            'home_shoot': r.home_shoot,
            'away_shoot': r.away_shoot,
            'home_start_member': r.home_start_member,
            'away_start_member': r.away_start_member,
            'game_start_at': datetime.datetime.strftime(r.game_start_at, '%Y/%m/%d %H:%M'),
            'weather': r.weather,
            'temperature': r.temperature,
            'referee': r.referee,
            'game_id': r.key().name(),
        })
    return render_json_response(return_data, mimetype='application/json')
