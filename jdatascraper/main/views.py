# -*- coding: utf-8 -*-

import datetime

from core.models import GameResult
from kay.utils import render_to_response, render_json_response


def index(request):
    return render_to_response('main/index.html', {'message': 'Hello'})


def gamestats(request, game_id):
    game_result = GameResult.get_by_key_name(game_id)
    return_data = {
        'series_number': game_result.series_number,
        'home_team': game_result.home_team,
        'away_team': game_result.away_team,
        'teams': game_result.teams,
        'home_director': game_result.home_director,
        'away_director': game_result.away_director,
        'home_score': game_result.home_score,
        'away_score': game_result.away_score,
        'home_shoot': game_result.home_shoot,
        'away_shoot': game_result.away_shoot,
        'home_start_member': game_result.home_start_member,
        'away_start_member': game_result.away_start_member,
        'game_start_at': datetime.datetime.strftime(game_result.game_start_at, '%Y/%m/%d %H:%M'),
        'weather': game_result.weather,
        'temperature': game_result.temperature,
        'referee': game_result.referee,
        'game_id': game_result.key().name(),
    }
    return render_json_response(return_data)