#The following is the pseudo code for the Hangman game to be coded in Python
"""
START
-generate secret word
-output initial blank drawing & hidden word
-ask player to guess letter
-if letter is in secret word:
    if hidden word is full player won:
    else:
        add letter to hidden word
else:
    -update drawing with +1 body party
-if letter already guessed:
    -warn player
-if body party part full drawn:
    -player lost

-ask player to play again
    if yes: go back to START
    else: END
"""

#Could be optimized / made simpler?
#I took a different way from the flowchart, made it more complete & concise
#Flowchat at Chapter 7 page 82