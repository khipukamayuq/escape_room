#!/usr/bin/env python
# -*- coding: utf-8 -*-
from item import Item

import re

class Room():
    def __init__(self):
        self.piano = Item("piano", "Clearly, an unused upright piano. The keyboard cover is closed.", "The piano appears quite dusty")
        self.desk = Item("desk", "An escritoire", "An ornate antique writing desk")
        self.door = Item("door", "Nothing seems to stand out.", "You stand before an arched, heavy wooden door with no doorknob or keyhole")

    def move_to(self, place):
        place_lower = place.lower()

        if re.search(r"^p[i][a][n][o]", place_lower):
            print("You move toward the piano")
        elif re.search(r"[e][s][k]", place_lower):
            print()
        elif re.search(r"^d[o][o][r]", place_lower):
            print()
        else:
            print("I'm afraid you can't do that.")

            
