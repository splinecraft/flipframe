import pymel.core as pm
"""Functions to make flipping back and forth between any two frames in Maya done easily with a hotkey

#####Command for setting the flip to frame:
from flipframe import flip
flip.update_flipframe()

#####Command for flip to (idealy use a press/release hotkey with these 2 commands:
import flipframe.flip
flip.flip_to()

#####Flip back:
import flipframe.flip
flip.flip_back()
"""

fframe = pm.currentTime(q=True)
baseframe = None
        
def run_flip():
    global fframe
    global baseframe
    fframe = pm.currentTime(q=True)
    baseframe = None
        
def flip_to():
    global fframe
    global baseframe
    baseframe = pm.currentTime(q=True)
    pm.currentTime(fframe, e=True)
    
def flip_back():
    global baseframe
    if  baseframe is not None:
        pm.currentTime(baseframe, e=True)
        
def update_flipframe():
    global fframe
    fframe = pm.currentTime(q=True)
        
if __name__ == "__main__":
    run_flip()