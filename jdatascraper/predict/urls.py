# -*- coding: utf-8 -*-
# predict.urls
# 

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='predict.views.index'),
  )
]

