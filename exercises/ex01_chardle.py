"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730669144"

word_guess: str= input("Enter a 5-character word ")
if len(word_guess) != 5 :
    print("Error: Word must contain 5 characters")
    exit

letter_guess1: str=input("Enter a single character ")
if len(letter_guess1) != 1 :
    print("Error: Character must be a single character.")

print("Searching for " + letter_guess1 + " in " + word_guess)

instances: int = 0

if str(word_guess)[0]==str(letter_guess1):
    print(letter_guess1 + " found at index 1") 
    instances= instances + 1
if str(word_guess)[1]==str(letter_guess1):
    print(letter_guess1 + " found at index 2")
    instances= instances + 1
if str(word_guess)[2]==str(letter_guess1):
    print(letter_guess1 + " found at index 3")
    instances= instances + 1
if str(word_guess)[3]==str(letter_guess1):
    print(letter_guess1 + " found at index 4")
    instances= instances + 1
if str(word_guess)[4]==str(letter_guess1):
    print(letter_guess1 + " found at index 5")
    instances= instances + 1


if int(instances) > 1 :
    print(str(int(instances)) + " instances of " + letter_guess1 + " found in " + word_guess)
    
else: 
    if int(instances) == 1:
        print("1 instance of " + letter_guess1 + " found in " + word_guess)
        
    else:
        print("No instances of " + letter_guess1 + " found in " + word_guess)

    