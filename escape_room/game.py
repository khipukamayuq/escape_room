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

    while new_room.door_open == False:
        new_prompt.main_prompt(new_player, new_room)
    else:
        print("Congratulations! Despite your blunders you escaped from the room!")



main()
