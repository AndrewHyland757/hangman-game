# Hangman


Many jobs nowadays, particularly in the world of software development, demand intense focus. Neuroscience has shown that when people have to focus
for long periods, cognitive resources are used up and performance declines. Luckily, there are ways to replenish! 
Hangman is a classic game that provides the perfect balance of light directed focus and fun to get those valuable recourses up again. 

This version of hangman is s Python terminal game that runs on Code Institute's mock terminal on Heroku.

![image](https://github.com/AndrewHyland757/hangman-game/assets/119887032/cb91f3e5-b43e-4593-b554-db8c9417d192)



![Screenshot of title](assets/images/responsive.jpg)



# [Link to live site](https://hangman-agame-app.herokuapp.com)
## How to play


The player enters their name, and the game begins. A word is generated randomly from a list, and as the player
guesses the correct letters, the word is revealed. Only five incorrect attempts are allowed. When the player
has two lives remaining, a hint is provided. At the end of the game, the player has the option to restart
and begin again with a new word.



## Planning


### Goals


* To create a fun and challenging game that is simple and engaging
* The game should be challenging enough to incite the player to continue playing.


### Logic Flow Chart


Before I began to write the code, I made a flow chart.


This helped answer questions like:


* How to determine the order of the processes
* How to deal with invalid inputs
* How to deal with incorrect inputs
![Screenshot of flow chart](assets/images/flow_chart.jpg)



## Features


### Title and name entry


* This is the first thing displayed. It gives an inviting presence to the game, with a familiar image of the hangman game.
![Screenshot of title](assets/images/title.jpg)


* The player is asked to enter their name, and a personal welcome is displayed.

![Screenshot of word input](assets/images/welcome.jpg)


### Main game display
* The player is presented with the hidden word in whice each correct letter is revealed.


![Screenshot of word input](assets/images/guess.jpg)


* The hangman's gallows image is gradually presented with each incorrect answer.


![Screenshot of word input](assets/images/incorrect_image.jpg)


* A helpful hint is given when there are two turns remaining.


![Screenshot of word input](assets/images/hint.jpg)


### Game over display
![Screenshot of game lose](assets/images/lose.jpg)
![Screenshot of game win](assets/images/win.jpg)
* This displayed the graphic of the end adding a dramatic finale to the game.


## Testing


I passed the code through a PEP8 Linter and fixed any errors.

## Bugs fixed

* Initally I had the word list outside the main game function, which didnt work with the restart function. 
* I added the hint to make the game more enjoyable. 


## Deployment


The project was deployed using Code Institutes mock terminal for Heroku.


Deployment steps:
* Create a new app in Heroku.
* Select "New" and "Create new app".
* Name the new app and click "Create new app".
* In Settings, select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
* Whilst still in "Settings", click "Reveal Config Vars" and input the following: KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files.
* Click on "Deploy" and select your deploy method and repository.
* Click "Connect" on selected repository.
* Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
* Heroku will now deploy the site.





