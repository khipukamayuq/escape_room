#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item:
    def __init__(self,
                 name,
                 description,
                 visible=False,
                 landing="none",
                 known="none",
                 used="none"):
        self.name = name
        self.description = description
        self.landing = landing
        self.used = used

    def examined(self):
        print(self.description)

    def used(self):
        print(self.used)
    
    def taken(self):
        print(f"You put the {self.name} in your inventory.")
