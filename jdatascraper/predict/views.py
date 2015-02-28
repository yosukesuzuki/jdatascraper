# -*- coding: utf-8 -*-
from kay.utils import render_to_response


def index(request):
    return render_to_response('predict/index.html', {'message': 'Hello'})
