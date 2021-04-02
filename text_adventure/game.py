#!/usr/bin/env python
# -*- coding: utf-8 -*-
from prompt import Prompt
from player import Player
from item import Item
from room import Room

def main():
    new_player = Player()
    new_room = Room()
    new_prompt = Prompt()

    new_prompt.preamble()



        
    #while True:
    new_prompt.main_prompt(new_player, new_room)

    # new_player.move(new_room)
    # new_player.used(new_room)


main()
