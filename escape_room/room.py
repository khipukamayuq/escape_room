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
                           visible=False,
                           used="")
        self.drawer = Item(name="drawer",
                           description="",
                           visible=False)
        self.tune = Item(name="song",
                         description="The notes you learned from the letter you found.",
                         known=False)
        self.door_open = False

    def __getitem__(self, attr_name):
        return self.__getattribute__(attr_name)

    def move_to(self, player_location, place):
        place_lower = place.lower()

        pattern = re.search(r"^p|e|^d", place_lower)

        template = "You move toward the "

        if pattern:
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
        else:
            print("Your legs wobble beneath you.")

    def examined(self, location):
        if location != "none":
            thing = self.__getitem__(location)

            if thing.name == "desk":
                self.drawer.visible = True

            print(thing.description)
        else:
            print("It's too hard to see from here.")

    def used(self, item_to_use):
        use_thing = self.__getitem__(item_to_use)

        if use_thing.name == "drawer":
            self.letter.visible = True
            print("There is a letter in the drawer:")
        elif use_thing.name == "letter":
            print(self.letter.description)
            self.tune.known = True
            print("""
                    You recognize the mnemonic but
                    can't place it. Maybe having a look
                    at something in here will jog your memory
                    """)
        else:
            print("Whatever you were expecting doesn't happen.")            
            
