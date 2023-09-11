import random
import time

heading = """
 _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
"""
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


def greeting():
    name = input("Enter your name to play: ").capitalize()
    #if name == "":
    #print("Please enter a valid name")
    while True:
            print(f"{name}...."):
            time.sleep(1)
            print("            ...lets play HANGMAN!!!")
            time.sleep(1)
            play_hangman()


def display_hangman(turns):
    """
    Function to show hangman figure based on number of turns left.
    """
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


lose = """
  __   __          _                _                _ _ 
  \ \ / /__  _   _( )_ __ ___    __| | ___  __ _  __| | |
   \ V / _ \| | | |/| '__/ _ \  / _` |/ _ \/ _` |/ _` | |
    | | (_) | |_| | | | |  __/ | (_| |  __/ (_| | (_| |_|
    |_|\___/ \__,_| |_|  \___|  \__,_|\___|\__,_|\__,_(_)
                                                                           
"""
win = """
  ____                            _         _       _   _                 _ 
 / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___| |
| |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
| |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
 \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                  |___/                                                    
 __   __            _ _             _ 
 \ \ / /__  _   _  | (_)_   _____  | |
  \ V / _ \| | | | | | \ \ / / _ \ | |
   | | (_) | |_| | | | |\ V /  __/ |_|
   |_|\___/ \__,_| |_|_| \_/ \___| (_)
                                      
                                      
"""

def restart_game():
    """
    Function to restart game.
    """
    play_again = input("Type 'yes' to play again :")
    if play_again == "yes":
        play_hangman()


def display_word(word, guessed_letters):
    """
    Function to display word in hidden form according to the amount of letters.
    Reveals the guessed letter if its correct. 
    """
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "
    return hidden_word


def is_guess_correct(word, guessed_letter):
    """
    Checks if the guessed letter is correct
    """
    return guessed_letter in word


def is_word_guessed(word, guessed_letters):
    """
    Checks if the word has been guessed completely
    """
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def play_hangman():
    """
    Main game function.
    Sets the number of turns to zero.
    Selects a random word and its corresponding hint from the dictionary. 
    This word is processed through a while loop. 
    """
    turns = 0
    guessed_letters = []
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
    
    word, hint = random.choice(list(word_list.items()))
    
    
    while turns < 6:
        print(display_hangman(turns))
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        """
        If statements to check if input letter is valid
        """
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        if not guess.isalpha(): 
            print("You must choose a letter!")
            continue
        if len(guess) > 1:
            print("Only one letter at a time. Try again!")

        guessed_letters.append(guess)
        if turns == 3:
            print("Hint: " + hint)
        if is_guess_correct(word, guess):
            print("Correct!")
        
            if is_word_guessed(word, guessed_letters):
                print(win)
                restart_game()
                break
        else:
            """
            Increases the turn value by one for each incorrect answer. 
            Sets the limit for the amount of turns.
            Finishes the game when this is reached with the option to 
            restart game. 
            """
            print("Incorrect!")
            turns += 1
            if turns == 6:
                print(display_hangman(turns))
                print(lose)
                restart_game()
                break

# Starts the game
greeting()


