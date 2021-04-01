#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, description, landing="none"):
        self.name = name
        self.description = description

    def examined(self):
        print(self.description)
    
