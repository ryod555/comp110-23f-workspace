"""EX02 - Chardle - A cute step toward Wordle."""
__author__ = "730669144"

secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess?")

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

while len(guess_word) != 6:  # while the length of the user inputed word is not 6
    guess_word = input("That was not 6 letters! Try again:")

wrong: bool = False  # declaring boolean variable and intializing it to false.
index: int = 0  # index will progress the while loop to cover each letter

while index < len(guess_word): 
    guess_char = guess_word[index]  # new variable that will reference the current letter being check in the loop
    if(secret_word[index] == guess_char): # guess character 
        print(green_box, end="")
    else:
        wrong = True  # sets the boolean to true if any of the characters is wrong, which will print "Not quite..."
        contained: bool = False  # new boolean which will determine if its yellow or white box
        x: int = 0 
        while x < 6:  # this while loop will check if the current character ("guess_char") is in the secret word
            if guess_char == secret_word[x]:
                contained = True 
            x += 1 
        if contained:  # if the boolean was set to true/ if the current character is in the secret word  
            print(yellow_box, end="")
        else:
            print(white_box, end="")
    index += 1  # adds 1 to the index after each loop to go to the next character
    
if wrong:  # if the boolean has been set to true (if it countains a yellow or white box), print
    print("\nNot quite. Play again soon!")

else:  # if the boolean is still false (only contains green boxes), print
    print("\nWoo! You got it!")