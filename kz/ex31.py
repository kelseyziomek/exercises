print "You enter a dark room with three doors. You can only choose one door. Which door do you choose?"
door = raw_input("> ")

if door == "1":
    print "There is a giant bear eating cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better anyways. Bear ran away."

if door == "2":
    print "You stare into the eyes of Cthulhu. You see the following:"
    print "1: Berries"
    print "2: My morning jacket"
    print "3: your future."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes. Good job!"

if door == "3":
    print "You have awakened the beast. Fight or flight?"
    darwinism = raw_input("> ")
    if darwinism.lower == "fight":
        print "You lose. Game over."
    elif darwinism.lower == "flight":
        print "You skipped leg day. Try again."
    else:
        print "Good idea. Just wait."

if door != "1" and door!= "2" and door!="3":
    print "If you can't choose a door, you aren't going to make it very far in life."
