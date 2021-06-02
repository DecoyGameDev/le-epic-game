#Owned by ht309553 on GitHub. Use this code if you want, but if you want you can email me and make me a
#contributer. My email is: ht309553@gmail.com (don't check email often, wait a few days and I will probably get back.)
#Also sorry for this sloppy code.
from adventurelib import *
print("When you DIE. Make sure to close out the game to reset. Dont use the ?, or help command. Because this might break the game. Also spoil it.")
print("A call is coming from your phone. You wonder if you should PICK UP.")
@when ("pick up")
def pickphone():
    say ("""
"Do you want to play a game?" The voice says. Do you say YES or NO? What is going on!
""")
@when ("yes")
def yes_kill():
    say ("""
"Yeah sure." You say, knowing this some sort of prank. Then you feel a sharp stab in your neck. You died.
""")
#my god deaths are sure common in this adventure
@when ("no")
def no_survive():
    say ("""
"No way." You say, it was probably just a prank call. You think, sweat starts to pour down your body. You wonder why he called, you wonder if you
should CALL BACK. Or just SIT DOWN.
""")
@when ("call back")
def call_backkill():
    say ("""
You go to pick up the phone and dial the number. You hear a slight peirce noise, your world becomes blank and you
pass out. Forever. You died.
""")
@when ("sit down")
def sit_down():
    say ("""
You sit down in confusion when you hear a knock at your door. You're tempted to OPEN DOOR, but after that
call pretty sceptical.
""")
@when ("open door")
def open_door_seq2():
    say ("""
You open the door and see nothing. From the DOOR NORTH you can see a bush rustling. You can also hear breathing. You can go BACK INSIDE. As that
will be the safest option, you think...
""")
@when ("back inside")
def backinside_kill():
    say ("""
You go back inside, and go up the stairs to bed. You forgot to shut the door! Waking up remembering, in a sweat. You rush back down
to see- nothing. You quickly shut it and put many extra locks. You look out the window at the bush and see that it is runined from someone running
through it. You feel a slit at the neck. You died!
""")
@when ("door north")
def door_north():
    say ("""
You walk over to the bush and see that it's... Invlated. You wonder if you should go BACK INSIDE, or OPEN BUSH.
""")
@when ("open bush")
def open_bush():
    say ("""
You open the bush and see a tiny rabbit. It runs out into the street. THE END!
""")
start()
