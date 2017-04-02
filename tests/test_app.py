#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for lambdaApi."""

import json
import lambdaapi.app as app


class TestApp:
    """TestApp class."""

    def test_echo_name(self):
        """Test echo_name function."""
        expected = json.dumps({'hello': 'world'})
        actual = json.dumps(app.echo_name("world"))
        assert expected == actual
