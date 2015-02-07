# -*- coding: utf-8 -*-
# scraper.urls
# 

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='scraper.views.index'),
  )
]

