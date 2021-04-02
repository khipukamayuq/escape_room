#!/usr/bin/env python
# -*- coding: utf-8 -*-
from item import Item

import re

class Room(Item):
    def __init__(self):
        self.piano = Item(name="piano",
                          description="Clearly, an unused upright piano. The keyboard cover is closed.",
                          visible=True,
                          landing="The piano appears quite dusty",
                          use={"key_cover": ""})
        self.desk = Item(name="desk",
                         description="An escritoire",
                         visible=True,
                         landing="An ornate antique writing desk",
                         use="")
        self.door = Item(name="door",
                         description="Nothing seems to stand out.",
                         visible=True,
                         landing="You stand before an arched, heavy wooden door with no doorknob or keyhole",
                         use="")
        self.letter = Item(name="letter",
                           description="""It reads: 'Every Good Boy Deserves Fudge'.
                           The first letter of each word is cirled in red.""",
                           takeable=True,
                           use="")

    def move_to(self, place):
        place_lower = place.lower()

        pattern = re.search(r"^p|e|^d", place_lower)

        template = "You move toward the "

        if pattern.group() == 'p':
            print(template + self.piano.name + " " + self.piano.landing)
        elif pattern.group() == 'e':
            print(template + self.desk.name + " " + self.desk.landing)
        elif pattern.group == 'd':
            print(template + self.door.name + " " + self.door.landing)
        else:
            print("That blow to your head may have done more damage than you thought.")

            
