# Snake Game
This is a classic Snake game built using Python and Pygame library. The objective of the game is to move a snake around the screen and eat as many food items as possible while avoiding collision with walls and the snake's own body.

# Getting Started
To run the game, you will need Python 3.x and Pygame library installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

To install Pygame, open a terminal or command prompt and enter the following command:

# Copy code
pip install pygame
Once you have installed Python and Pygame, you can run the game by opening a terminal or command prompt, navigating to the directory where the game files are located, and entering the following command:

# css
Copy code
python main.py
How to Play
When you start the game, you will see a snake and food items on the screen. To move the snake, use the arrow keys on your keyboard. The snake will move in the direction of the arrow key that you press.

If the snake collides with the wall or its own body, the game will end. You start the game with three lives, and if you lose all your lives, the game will end.

Your score is displayed at the top of the screen, and it increases each time you eat a food item. When the snake eats a food item, its body grows longer.

# Customization
If you want to customize the game, you can modify the following variables in the config.py file:

WINDOW_WIDTH and WINDOW_HEIGHT: The width and height of the game window, in pixels.
SNAKE_SPEED: The speed of the snake.
FOOD_COUNT: The number of food items on the screen.
FOOD_POINTS: The number of points you earn for eating a food item.
You can also modify the images used in the game by replacing the .png files in the images folder..
