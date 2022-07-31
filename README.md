# RPSLS-Rock-Paper-Scissors-Lizard-Spock-Game-py

**RPSLS Rock Paper Scissor Lizarf Spock Game Rule**
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock

**Technologies**
Python, Visual Studio Code w/ Debugger, Git/GitHub

**Algorithm for RPSLS:**
Step 1: Display the rules of the game
Step 2: Ask how many human players will be playing ? (from 0 to 2)
Step 4: Game starts, If there are no human players, generated AI players gestures randomly
If there are any human player, let human play choose gesture first, then display AI player gesture randomly
Step 5: Display the winner for the round, winner’s counter accumulates by one
Step 6: Repeat step 4 and 5, if any of the winner counter reaches 2, otherwise goes back to 4
Step 7: Display final winner
Step 8: Ask user “Do you want to play again? (Enter y/n)”
Step 9: if User chooses n, display” Thanks for playing RPSLS game”
if user chooses y, goes back to step 2

**File Structure**

- main.py: main file to run the game
- game.py: contains the algorithm for the game
- player.py: contais parent class Player, each player has a name, and can access the gesture stores in the gesture list
- human.py: child class of Player, each human player selects its own gesture from the gesture list
- ai.py: child class of Player, each ai player generates its gesture randomly
- utility.py: contains functions for general use
