# -*- coding: utf-8 -*-

from scraper.scraper import get_game_id
from kay.ext.testutils.gae_test_base import GAETestBase


class GetGameIDTest(GAETestBase):
    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_get_game_id(self):
        game_ids = get_game_id(2014)
        self.assertEquals(game_ids[0], '15671')
