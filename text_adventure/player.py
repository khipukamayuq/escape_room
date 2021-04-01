#!/usr/bin/env python
# -*- coding: utf-8 -*-
from item import Item

class Player:
    def __init__(self):
        self.inventory = []

    def examine(self, item):
        print(item.examined())

    def move(self, direction):
        pass

    def take(self, item):
#          try:
        inventory.append(item)

    def use(self, item):
        pass
