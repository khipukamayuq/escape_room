#!/usr/bin/env python
# -*- coding: utf-8 -*-
from item import Item
from room import Room

import re

class Player:
    def __init__(self, location="none"):
        self.inventory = []
        self.location = location

    def examine(self, room):
        location = self.location 
        room.examined(location)

    def move(self, room):
        location = self.location

        place = input("""To where would you like to move?

                             (p)iano d(e)sk (d)oor 
                        """)
        try:
            moved = room.move_to(location, place)
        except:
            print("""
                    You catch yourself from falling. Maybe
                    you should lie back down on the floor.
                  """)
        
        self.location = moved
    
    def take(self):
        inventory.append(item)

    def use(self, room):
        location = self.location

        if location == "desk" and room.drawer.visible == True:
            to_use = input("""
                            Open the drawer?

                            (y)es  (n)o
                           """)

            drawer_answer = re.search(r"^y", to_use.lower())

            if drawer_answer:
                if drawer_answer.group() == "y":
                    room.used("drawer")
                else:
                    print("Maybe you don't want to escape?")

                open_letter = input("""
                                        Read the letter?

                                            (y)es  (n)o
                                   """)

                letter_answer = re.search(r"^y", open_letter.lower())

                if letter_answer:
                    if letter_answer.group() == "y":
                        room.used("letter")
                    else:
                        print("Don't give up now!")
            else:
                    print("You should stop wasting time.")

        elif location == "piano" and room.tune.known == True:
            print("""
                    The circled letters on the note suddenly make sense
                    when looking at the worn piano keys! 'Every Good Boy
                    Deserves Fudge' might be the keys 'E,' 'G,' 'B,' 'D,'
                    'F'.
                  """)

            play_tune = input("""
                                Would you like to play the keys?

                                    (y)es  (n)o
                              """)

            play_answer = re.search(r"^y", play_tune.lower())

            if play_answer:
                if play_answer.group() == "y":
                    print("""
                            You tickle the ivories as best you can.
                            Suddenly the door swings open.

                            You're free!!
                        """)
                    room.door_open = True
                else:
                    print("Now is not the time to be self conscious of your playing!")

        else:
            print("There's nothing obvious to use.")

