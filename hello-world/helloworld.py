# -*- coding: utf-8 -*-
"""
    helloworld.py

    :copyright: (c) 2015 by Prakash Pandey
    :license: see LICENSE for more details.
"""

from trytond.model import ModelSQL, ModelView, fields

__all__ = ['HelloWorld']


class HelloWorld(ModelSQL, ModelView):
    "Hello World"
    __name__ = "hello.world"

    name = fields.Char("Name", required=True)
