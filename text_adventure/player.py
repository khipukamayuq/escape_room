#!/usr/bin/env python
# -*- coding: utf-8 -*-
from item import Item
from room import Room

class Player:
    def __init__(self, location="none"):
        self.inventory = []
        self.location = location

    def examine(self):
        item = input("""
                        What would you like to investigate?

                        
                     """)
        print(item.examined())

    def move(self, room):
        place = input("""To where would you like to move?

                             (p)iano d(e)sk (d)oor 
                        """)
        try:
            print("in the try")
            print(room)
            moved = room.move_to(place)
            self.location = moved
        except:
            print("""
                    You catch yourself from falling. Maybe
                    you should lie back down on the floor.
                  """)

    def take(self):
        inventory.append(item)

    def use(self):
        if room.piano:
            room.piano.used()
        elif room.desk:
            room.desk.used()
        elif room.letter:
            room.letter.used()
        else:
            print("Nothing happened.")

