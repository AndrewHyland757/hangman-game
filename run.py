import random
import time


# Display game heading & image
heading = ("HANGMAN")
print(heading)
print("""
     __________
      |      |
      |      O     
      |     /|\     
      |     / \    
      |
      |
      |
     ===========
     """)

time.sleep(1)

# Player name entry
name = input("Enter your name to play: \n").capitalize()
print(f"{name}....")
time.sleep(1)
print("            ...lets play HANGMAN!!!")
time.sleep(1)

# Function to show hangman figure bases on number of guesses left
def display_hangman(turns):
    hangman_pics = ["""
     __________
      |      |
      |         
      |        
      |      
      |
      |
      |
     ===========""",
        """
     __________
      |      |
      |      O     
      |        
      |        
      |
      |
      |
     ===========""",
        """
     __________
      |      |
      |      O     
      |     /  
      |       
      |
      |
      |
     ===========""",
        """
     __________
      |      |
      |      O     
      |     /|   
      |        
      |
      |
      |
     ===========""",
        """
     __________
      |      |
      |      O     
      |     /|\     
      |        
      |
      |
      |
     ===========""",
        """
     __________
      |      |
      |      O     
      |     /|\     
      |     /    
      |
      |
      |
     ===========""",
        """
     __________
      |      |
      |      O     
      |     /|\     
      |     / \    
      |
      |
      |
     ==========="""]
    
    return hangman_pics[turns]

# Function to restart game
def restart_game():
  play_again = input("Type 'yes' to play again: \n")
  if play_again == "yes":
    play_hangman()

# Display the word using hidden letters
def display_word(word, guessed_letters):
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "
    return hidden_word

# Check if the guessed letter is correct
def is_guess_correct(word, guessed_letter):
    return guessed_letter in word

# Check if the word has been guessed completely
def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Main game function
def play_hangman():
    turns = 0
    guessed_letters = []
 
  # List of words and hints 
    word_list = {
      "python" : "A type of snake",
      "zephyr" : "A type of wind",
      "hangman" : "A word-guessing game",
      "blunder" : "Another word for a mistake",
      "ignition" : "The device used to start a car",
      "devour" : "To eat hungrily or quickly",
      "fjord" : "A long, deep, narrow body of water that reaches far inland",
      "paradox" : "A seemingly absurd or contradictory statement",
      "maple" : "A type of tree",
      "archipelago" : "A group of islands"
    }
    
    # Randomally select word and its hint
    word, hint = random.choice(list(word_list.items()))
   
    # End of game text display
    lose = ("You're dead!\n The word was : " + word)
    win = ("Congratulations! You guessed the word : " + 
    word + "\n You live !")
   
    # Main game loop
    while turns < 6:
        print(display_hangman(turns))
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: \n").lower()
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        if not guess.isalpha(): 
            print("You must choose a letter!")
            continue
        if len(guess) > 1:
            print("Only one letter at a time. Try again!")
        guessed_letters.append(guess)
        if turns == 4:
            print("Hint: " + hint)
        if is_guess_correct(word, guess):
            print("Correct!")
        
            if is_word_guessed(word, guessed_letters):
                print(win)
                restart_game()
                break
        else:
            print("Incorrect!")
            turns += 1
            if turns == 6:
                print(display_hangman(turns))
                print(lose)
                restart_game()
                break

# Start the game
play_hangman()