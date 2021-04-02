#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import Player
from item import Item
from room import Room

def main():

    new_player = Player()
    
    new_room = Room()

    key = Item("letter",
               """It reads: 'Every Good Boy Deserves Fudge'.
               The first letter of each word is cirled in red.""")

        
    #while True:
    # some sort of intro/setup
    new_player.move(new_room)


main()
