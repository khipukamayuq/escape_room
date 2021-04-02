#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item:
    def __init__(self,
                 name,
                 description,
                 visible=False,
                 takeable=False,
                 landing="none",
                 use="none"):
        self.name = name
        self.description = description
        self.landing = landing
        self.use = use

    def examined(self):
        print(self.description)

    def used(self):
        print(self.use[1])
    
    def taken(self):
        print(f"You put the {self.name} in your inventory.")
