# -*- coding: utf-8 -*-
from __future__ import absolute_import

counter = 0

def my_initializer(context):
    global counter
    counter += 1
    return counter

def my_handler(event, context):
    global counter
    counter += 1
    return counter