# random number generator
 the program generates a random number between 1 and 100. The player needs to guess the number, and the program provides hints if the guess is too low or too high. The game continues until the player guesses the correct number
The program generates a random number using the random.randint() function, which takes a range of numbers (in this case, 1 to 100) and selects a random integer within that range.

The game starts with a welcome message.

Inside the game loop, the player is prompted to enter their guess using the input() function. The input is converted to an integer using int().

The player's guess is compared to the randomly generated number. If the guess is lower than the number, the program displays "Too low!". If the guess is higher, the program displays "Too high!".

If the player's guess is equal to the generated number, the program displays a congratulatory message along with the actual number and the number of attempts it took to guess correctly.

The game continues until the player guesses the correct number, at which point the loop is exited using the break statement.

This simple game allows players to test their guessing skills and have fun trying to guess the randomly generated number within the given range.