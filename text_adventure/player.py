#!/usr/bin/env python
# -*- coding: utf-8 -*-
from item import Item
from room import Room

class Player:
    def __init__(self):
        self.inventory = []

    def examine(self, item):
        print(item.examined())

    def move(self, room):
        place = input("""To where would you like to move?

                             (p)iano d(e)sk (d)oor 
                        """)
        room.move_to(place)

    def take(self, item):
#          try:
        inventory.append(item)

    def use(self, item):
        pass
