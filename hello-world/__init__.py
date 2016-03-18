# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Prakash Pandey
    :license: see LICENSE for details.
"""
from trytond.pool import Pool
from helloworld import HelloWorld


def register():
    Pool.register(
    	HelloWorld,
        module='helloworld', type_='model'
    )
