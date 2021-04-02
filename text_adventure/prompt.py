#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import Player

import re

class Prompt():
    def preamble(self):
        print("""
            You awaken with a gasp and a sudden realization
            of a splitting headache. You're on the floor of
            a sparsely decorated room. An unusually large
            wooden door catches your eye. It seems you may
            be locked in here. Perhaps the piano or desk
            may contain some answers.
        """)

    def main_prompt(self, player, room):
        action = input("""What would you like to do?
            e(x)amine  (m)ove  (t)ake  (u)se
        """)

        pattern = re.search(r"x|^m|^t|^u", action)

        if pattern.group() == "x":
            return player.examine()
        elif pattern.group() == "m":
            return player.move(room) 
        elif pattern.group() == "t":
            return player.take()
        elif pattern.group() == "u":
            return player.use()
        else:
            print("You're not making any sense")
            
