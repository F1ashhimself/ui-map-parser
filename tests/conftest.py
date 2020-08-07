# -*- coding: utf-8 -*-

__author__ = 'f1ashhimself@gmail.com'

from pathlib import Path

import pytest

from ui_map_parser import UIMapParser


@pytest.fixture(scope='function')
def ui_map_parser(request):
    language = None
    if hasattr(request, 'param'):
        language = request.param

    return UIMapParser(Path(__file__).parent / 'test_data', language=language)
