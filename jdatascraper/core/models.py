# -*- coding: utf-8 -*-
# core.models

from google.appengine.ext import db

# Create your models here.


class GameId(db.Model):
    '''
    set game id as key name
    '''
    game_id = db.StringProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)


class GameResult(db.Model):
    result = db.StringProperty(required=True, choices=('home_win', 'draw', 'away_win'))
    teams = db.StringListProperty()
    series_number = db.IntegerProperty()
    home_team = db.StringProperty(required=True)
    away_team = db.StringProperty(required=True)
    home_director = db.StringProperty(required=True)
    away_director = db.StringProperty(required=True)
    home_score = db.IntegerProperty(default=0)
    away_score = db.IntegerProperty(default=0)
    home_shoot = db.IntegerProperty(default=0)
    away_shoot = db.IntegerProperty(default=0)
    home_start_member = db.TextProperty(default="")
    away_start_member = db.TextProperty(default="")
    game_start_at = db.DateTimeProperty()
    weather = db.StringProperty(default="")
    temperature = db.FloatProperty()
    referee = db.StringProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)
