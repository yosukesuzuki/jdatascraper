# -*- coding: utf-8 -*-
# core.urls
# 

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='core.views.index'),
  )
]

