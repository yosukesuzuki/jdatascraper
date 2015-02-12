# -*- coding: utf-8 -*-

import datetime

from kay.ext.testutils.gae_test_base import GAETestBase
from scraper.scrap import get_game_id, scrap_game_data
from scraper.game_data import test_game_data
from scraper.views import save_game_id, save_game_result
from core.models import GameId, GameResult


class GetGameIDTest(GAETestBase):
    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_get_game_id(self):
        game_ids = get_game_id(2014)
        self.assertEquals(game_ids[0], '15671')
        game_ids = get_game_id(2014)
        save_game_id(game_ids)
        game_id_object = GameId.get_by_key_name('15671')
        self.assertEquals(game_id_object.game_id, '15671')
        game_count = GameId.all().count(limit=5000)
        self.assertEquals(game_count, 768)


class ScrapGameDataTest(GAETestBase):
    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_scrap_game_data(self):
        result = scrap_game_data(test_game_data)
        self.assertEquals(result['series_number'], 1)
        self.assertEquals(result['home_team'], u'セレッソ大阪')
        self.assertEquals(result['away_team'], u'サンフレッチェ広島')
        self.assertEquals(result['teams'][0], u'セレッソ大阪')
        self.assertEquals(result['home_director'], u'ランコ　ポポヴィッチ')
        self.assertEquals(result['away_director'], u'森保　一')
        self.assertEquals(result['home_score'], 0)
        self.assertEquals(result['away_score'], 1)
        self.assertEquals(result['home_shoot'], 12)
        self.assertEquals(result['away_shoot'], 10)
        self.assertEquals(result['home_start_member'].split(',')[0], u'キム　ジンヒョン')
        self.assertEquals(result['home_start_member'].split(',')[-1], u'フォルラン')
        self.assertEquals(result['away_start_member'].split(',')[0], u'林　卓人')
        self.assertEquals(result['away_start_member'].split(',')[-1], u'佐藤　寿人')
        self.assertEquals(result['game_start_at'], datetime.datetime.strptime('2014/03/01 14:04', '%Y/%m/%d %H:%M'))
        self.assertEquals(result['weather'], u'雨')
        self.assertEquals(result['temperature'], 12.3)
        self.assertEquals(result['referee'], u'家本　政明')
        result['game_id'] = '15671'
        save_game_result([result])
        game_result_15671 = GameResult.get_by_key_name('15671')
        self.assertEquals(game_result_15671.home_team, u'セレッソ大阪')
