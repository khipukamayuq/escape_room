#!/usr/bin/env python
# -*- coding: utf-8 -*-
from item import Item

import re

class Room(Item):
    def __init__(self):
        self.piano = Item(name="piano",
                          description="A well-worn upright piano. The keyboard cover is open. Several keys appear more worn than others.",
                          visible=True,
                          landing="The piano appears quite dusty. You wonder if anyone has played this recently.")
        self.desk = Item(name="desk",
                         description="An escritoire. There seems to be only a single drawer.",
                         visible=True,
                         landing="An ornate antique writing desk",
                         used="You open the drawer revealing an unaddressed letter.")
        self.door = Item(name="door",
                         description="Nothing seems to stand out.",
                         visible=True,
                         landing="You stand before an arched, heavy wooden door with no doorknob or keyhole")
        self.letter = Item(name="letter",
                           description="""
                                        It reads: 'Every Good Boy Deserves Fudge'.
                                        The first letter of each word is cirled in red.
                                        """,
                           takeable=True,
                           visible=False,
                           used="")
        self.drawer = Item(name="drawer",
                           description="",
                           visible=False)
        self.tune = Item(name="song",
                         description="The notes you learned from the letter you found.",
                         takeable=True)

    def __getitem__(self, attr_name):
        return self.__getattribute__(attr_name)

    def move_to(self, player_location, place):
        place_lower = place.lower()

        pattern = re.search(r"^p|e|^d", place_lower)

        template = "You move toward the "

        if pattern.group() == 'p':
            print(template + self.piano.name + " " + self.piano.landing)
            new_location = self.piano.name

            return new_location

        elif pattern.group() == 'e':
            print(template + self.desk.name + " " + self.desk.landing)
            new_location = self.desk.name

            return new_location

        elif pattern.group() == 'd':
            print(template + self.door.name + " " + self.door.landing)
            new_location = self.door.name

            return new_location

        else:
            print("""
                    You stagger in-place. That blow to your head may
                    have done more damage than you thought.
                  """)

    def examined(self, location):
        if location != "none":
            thing = self.__getitem__(location)

            if thing.name == "desk":
                self.drawer.visible = True

            print(self.drawer.visible)
            print(thing.description)
        else:
            print("It's too hard to see from here.")

    def used(self):
        thing = self.__getitem__(item)

        if thing.name == "drawer":
            self.letter.visible = True
            print("There is a letter in the drawer:")
        elif thing.name == "letter":
            print(self.letter.description)
            taken(self.tune)


        #  elif thing.name == "piano":
        #      pass
        #  else:
            
    def taken(self, item):
        print(f"You remember the tune for later... just in case.")
            
