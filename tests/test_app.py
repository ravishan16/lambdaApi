#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lambdaapi.app as app

class TestApp:
    def test_count(self):
        assert 1 == app.count()
