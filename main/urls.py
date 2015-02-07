# -*- coding: utf-8 -*-
# main.urls
# 

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='main.views.index'),
  )
]

