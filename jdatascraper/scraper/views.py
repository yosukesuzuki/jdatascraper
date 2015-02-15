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
    for game_result in game_results:
        # import pdb; pdb.set_trace()
        entity = GameResult(key_name=game_result['game_id'], **game_result)
        entity.put()


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


def set_game_stats(request):
    for entity in GameId.all().fetch(1000):
        set_latest_stats(entity.key().name())
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
    return render_json_response(return_data)


def set_latest_stats(game_id):
    game_result = GameResult.get_by_key_name(game_id)
    home_team_results = GameResult.all().filter(
        u'teams =', game_result.home_team).filter(u'game_start_at <', game_result.game_start_at).order(
        '-game_start_at').fetch(5)
    home_team_scores = []
    home_team_shoots = []
    home_team_wins = []
    home_team_draws = []
    home_team_losts = []
    for home_team_result in home_team_results:
        if game_result.home_team == home_team_result.home_team:
            home_team_scores.append(home_team_result.home_score)
            home_team_shoots.append(home_team_result.home_shoot)
            if home_team_result.result == 'home_win':
                home_team_wins.append(1)
                home_team_draws.append(0)
                home_team_losts.append(0)
            elif home_team_result.result == 'draw':
                home_team_wins.append(0)
                home_team_draws.append(1)
                home_team_losts.append(0)
            elif home_team_result.result == 'away_win':
                home_team_wins.append(0)
                home_team_draws.append(0)
                home_team_losts.append(1)
        elif game_result.home_team == home_team_result.away_team:
            home_team_scores.append(home_team_result.away_score)
            home_team_shoots.append(home_team_result.away_shoot)
            if home_team_result.result == 'home_win':
                home_team_wins.append(0)
                home_team_draws.append(0)
                home_team_losts.append(1)
            elif home_team_result.result == 'draw':
                home_team_wins.append(0)
                home_team_draws.append(1)
                home_team_losts.append(0)
            elif home_team_result.result == 'away_win':
                home_team_wins.append(1)
                home_team_draws.append(0)
                home_team_losts.append(0)
    away_team_results = GameResult.all().filter(
        u'teams =', game_result.away_team).filter('game_start_at <', game_result.game_start_at).order(
        '-game_start_at').fetch(5)
    away_team_scores = []
    away_team_shoots = []
    away_team_wins = []
    away_team_draws = []
    away_team_losts = []
    for away_team_result in away_team_results:
        if game_result.away_team == away_team_result.home_team:
            away_team_scores.append(away_team_result.home_score)
            away_team_shoots.append(away_team_result.home_shoot)
            if away_team_result.result == 'home_win':
                away_team_wins.append(1)
                away_team_draws.append(0)
                away_team_losts.append(0)
            elif away_team_result.result == 'draw':
                away_team_wins.append(0)
                away_team_draws.append(1)
                away_team_losts.append(0)
            elif away_team_result.result == 'away_win':
                away_team_wins.append(0)
                away_team_draws.append(0)
                away_team_losts.append(1)
        elif game_result.away_team == away_team_result.away_team:
            away_team_scores.append(away_team_result.away_score)
            away_team_shoots.append(away_team_result.away_shoot)
            if away_team_result.result == 'home_win':
                away_team_wins.append(0)
                away_team_draws.append(0)
                away_team_losts.append(1)
            elif away_team_result.result == 'draw':
                away_team_wins.append(0)
                away_team_draws.append(1)
                away_team_losts.append(0)
            elif away_team_result.result == 'away_win':
                away_team_wins.append(1)
                away_team_draws.append(0)
                away_team_losts.append(0)
    game_result.home_score_last1 = sum(home_team_scores[:1])
    game_result.away_score_last1 = sum(away_team_scores[:1])
    game_result.home_score_last3 = sum(home_team_scores[:3])
    game_result.away_score_last3 = sum(away_team_scores[:3])
    game_result.home_score_last5 = sum(home_team_scores[:5])
    game_result.away_score_last5 = sum(away_team_scores[:5])
    game_result.home_shoot_last1 = sum(home_team_shoots[:1])
    game_result.away_shoot_last1 = sum(away_team_shoots[:1])
    game_result.home_shoot_last3 = sum(home_team_shoots[:3])
    game_result.away_shoot_last3 = sum(away_team_shoots[:3])
    game_result.home_shoot_last5 = sum(home_team_shoots[:5])
    game_result.away_shoot_last5 = sum(away_team_shoots[:5])
    game_result.home_win_last1 = sum(home_team_wins[:1])
    game_result.away_win_last1 = sum(away_team_wins[:1])
    game_result.home_win_last3 = sum(home_team_wins[:3])
    game_result.away_win_last3 = sum(away_team_wins[:3])
    game_result.home_win_last5 = sum(home_team_wins[:5])
    game_result.away_win_last5 = sum(away_team_wins[:5])
    game_result.home_draw_last1 = sum(home_team_draws[:1])
    game_result.away_draw_last1 = sum(away_team_draws[:1])
    game_result.home_draw_last3 = sum(home_team_draws[:3])
    game_result.away_draw_last3 = sum(away_team_draws[:3])
    game_result.home_draw_last5 = sum(home_team_draws[:5])
    game_result.away_draw_last5 = sum(away_team_draws[:5])
    game_result.home_lost_last1 = sum(home_team_losts[:1])
    game_result.away_lost_last1 = sum(away_team_losts[:1])
    game_result.home_lost_last3 = sum(home_team_losts[:3])
    game_result.away_lost_last3 = sum(away_team_losts[:3])
    game_result.home_lost_last5 = sum(home_team_losts[:5])
    game_result.away_lost_last5 = sum(away_team_losts[:5])
    game_result.put()
