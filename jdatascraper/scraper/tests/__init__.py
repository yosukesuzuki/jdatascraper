# -*- coding: utf-8 -*-

from kay.ext.testutils.gae_test_base import GAETestBase
from scraper.scrap import get_game_id, scrap_game_data
from scraper.game_data import test_game_data
# from scraper.views import save_game_id
# from core.models import GameId


class GetGameIDTest(GAETestBase):
    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_get_game_id(self):
        game_ids = get_game_id(2014)
        self.assertEquals(game_ids[0], '15671')


'''
class SaveGameIDTest(GAETestBase):
    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_save_game_id(self):
        game_ids = get_game_id(2014)
        save_game_id(game_ids)
        game_id_object = GameId.get_by_key_name('15671')
        self.assertEquals(game_id_object.game_id, '15671')
        game_count = GameId.all().count(limit=5000)
        self.assertEquals(game_count, 768)
'''


class ScrapGameDataTest(GAETestBase):
    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_scrap_game_data(self):
        result = scrap_game_data(test_game_data)
        self.assertEquals(result['series_number'], 1)
