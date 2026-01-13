
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
    +---+
    |   |
    O   |
    |   |
   / \  |
        |
        |
=========''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
=========''', r'''
    +---+
    |   |
        |
        |
        |
        |
=========''']
word_list=["mango","apple","banana","papaya","peach","grapes","orange","kiwi","watermelon","strawberry"]
import random 
print("welcome to hangman game")
chosen_word=random.choice(word_list)
lives=6
guessed_letters=set()
print("_ "*len(chosen_word))
while lives>0:
    guess=input("enter a letter for the chosen word: ").lower()
    if not guess.isalpha():
        print("Please type a letter.")
        continue
    if len(guess) != 1 :
        print("Enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    display=""    
    if guess in chosen_word:
        guessed_letters.add (guess)
        for letter in chosen_word:
            if letter in guessed_letters:
                display+=letter
            else:
                display+="_"
        print(display) 
        
    else:
        lives-=1
        print(f"wrong guess. you have {lives} lives left.") 
        print(stages[lives])     
    if"_" not in display:
        print("congratulations! you guessed the word correctly.")
        break
    if lives==0:
        print(f"you lost! the correct word was {chosen_word}.")
        break