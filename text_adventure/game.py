#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import Player
from item import Item
from room import Room

def main():

    new_player = Player()
    
    new_room = Room()

    key = Item("key", "a small brass key")
    #  items = [("key", "a small brass key"),
    #           ("letter", "It reads: 'how about a riddle'")]

#      for item in items:
        
    #while True:
    # some sort of intro/setup
    # run script
    # capture user input
    print('This is the game.')
    print(new_player)
    print(key)
    new_player.examine(key)    
    new_player.move(new_room)


main()
