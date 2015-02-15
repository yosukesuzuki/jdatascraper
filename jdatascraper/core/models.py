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
    teams = db.StringListProperty()
    division = db.IntegerProperty()
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
    home_score_last1 = db.IntegerProperty(default=0)
    away_score_last1 = db.IntegerProperty(default=0)
    home_score_last3 = db.IntegerProperty(default=0)
    away_score_last3 = db.IntegerProperty(default=0)
    home_score_last5 = db.IntegerProperty(default=0)
    away_score_last5 = db.IntegerProperty(default=0)
    home_shoot_last1 = db.IntegerProperty(default=0)
    away_shoot_last1 = db.IntegerProperty(default=0)
    home_shoot_last3 = db.IntegerProperty(default=0)
    away_shoot_last3 = db.IntegerProperty(default=0)
    home_shoot_last5 = db.IntegerProperty(default=0)
    away_shoot_last5 = db.IntegerProperty(default=0)
    home_win_last1 = db.IntegerProperty(default=0)
    away_win_last1 = db.IntegerProperty(default=0)
    home_win_last3 = db.IntegerProperty(default=0)
    away_win_last3 = db.IntegerProperty(default=0)
    home_win_last5 = db.IntegerProperty(default=0)
    away_win_last5 = db.IntegerProperty(default=0)
    home_draw_last1 = db.IntegerProperty(default=0)
    away_draw_last1 = db.IntegerProperty(default=0)
    home_draw_last3 = db.IntegerProperty(default=0)
    away_draw_last3 = db.IntegerProperty(default=0)
    home_draw_last5 = db.IntegerProperty(default=0)
    away_draw_last5 = db.IntegerProperty(default=0)
    home_lost_last1 = db.IntegerProperty(default=0)
    away_lost_last1 = db.IntegerProperty(default=0)
    home_lost_last3 = db.IntegerProperty(default=0)
    away_lost_last3 = db.IntegerProperty(default=0)
    home_lost_last5 = db.IntegerProperty(default=0)
    away_lost_last5 = db.IntegerProperty(default=0)
    updated_at = db.DateTimeProperty(auto_now=True)
    created_at = db.DateTimeProperty(auto_now_add=True)

    @property
    def result(self):
        if self.home_score > self.away_score:
            return 'home_win'
        if self.home_score == self.away_score:
            return 'draw'
        if self.home_score < self.away_score:
            return 'away_win'
