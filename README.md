## CLI text-based escape room 

Code: <Louisville> Jan 2021 Python Final Project

Simple interactive fiction/text-based game.


### Features implemented:

* master loop
* create class and instantiate an object of that class; populate with data
* create and call 3 functions/methods; set values dynamically. couple `returns` that bring back data used elsewhere
* use regex for text validation
* (a stretch) implemented `___getitem___` within Room class and access items using it; so sorta a dictionary that I'm retrieving values from

### Use

Clone the repo. Only need a Python installation. This was written using Python 3.9.2.

`cd` into the app folder and run `python game.py`.

Starts the loop that is the game. There is a main prompt that runs. Player can make
a selection for one of three actions. Some actions require a target (i.e. a second input)
and will prompt further when necessary. Player is free to explore the room and 
examine or use items in the room. Certain action/options/story-advancement are
only available when conditions have been met.

This is a huge slop of sphagetti. Written primarily stream-of-consciousness over the last 
48hrs or so. I'm so sorry.

