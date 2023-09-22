"""Exercise 3, Wordle for real"""
__author__ = "730669144"


white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def contains_char(word: str, guess_char: str) -> bool:
    """Returns true if the single character string is found at any index of the first string"""
    assert len(guess_char) == 1
    idx: int = 0
    while idx < len(word):
        if guess_char == word[idx]: 
            return True
        idx += 1

    return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Returns a string of emojis coordinating to the right letters"""
    assert len(guess_word) == len(secret_word)
    emojis: str = ""
    idx: int = 0
    while idx < len(guess_word):
        if guess_word[idx] == secret_word[idx]:
            emojis += green_box
        else:
            if contains_char(secret_word, guess_word[idx]):
                emojis += yellow_box
            else:
                emojis += white_box
        idx += 1
    return emojis
    
def input_guess(length: int) -> str:
    """Given an integer for the length of the word, will prompt the user for a guess and continue prompting until the length is correct"""
    guess_word = input(f"Enter a {length} letter word: ") # prompts the player to enter a word
    while len(guess_word) != length: # while the length of the guess word isnt equal to length of the secret word
        guess_word = input(f"That wasn't {length} chars! Try again: ")
    return str(guess_word)
    
def main() -> None:
    """The entrypoint of the program and main game loop."""
    tries: int = 0
    max_tries: int = 5

    the_word: str = ("poop") # THE SECRET WORD

    length: int = len(the_word) # creates a variable adapting to the length of the word


    while tries < max_tries: 
        print(f"==Turn {tries + 1}/6==")
        guess_word: int = input_guess(length) # creates a variable to the word guessed by the player, locally to change with each loop and continue to prompt the player
        print(emojified(guess_word, the_word)) # invokes the function emojified
        emojis: str = (emojified(guess_word, the_word)) # creating the outputted emojis into a variable to reference

        if str(emojis) == ("\U0001F7E9"*int(length)): # if the outputted emojis is the same as [length] green squares, print the winning message 
            print(f"You won in {tries + 1} turns!")
            tries = max_tries + 1  # exits the while loop
        tries += 1
    if tries == max_tries: # since tries is 1 plus greater than the max tries when you win, if the player reaches the max amount of tries, prints the losing message
        print("6/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()    
    
