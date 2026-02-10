import tkinter as tk
from tkinter import messagebox
import random
from collections import deque

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        # Game constants
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 600
        self.GRID_SIZE = 20
        self.GRID_WIDTH = self.WINDOW_WIDTH // self.GRID_SIZE
        self.GRID_HEIGHT = self.WINDOW_HEIGHT // self.GRID_SIZE
        
        # Game variables
        self.snake = deque([(self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2)])
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        self.paused = False
        self.speed = 100  # milliseconds
        
        # Create canvas
        self.canvas = tk.Canvas(
            root,
            width=self.WINDOW_WIDTH,
            height=self.WINDOW_HEIGHT,
            bg="black"
        )
        self.canvas.pack()
        
        # Bind keys to root window for better key capture
        self.root.bind("<Up>", self.on_key_press)
        self.root.bind("<Down>", self.on_key_press)
        self.root.bind("<Left>", self.on_key_press)
        self.root.bind("<Right>", self.on_key_press)
        self.root.bind("<space>", self.on_key_press)
        self.root.bind("r", self.on_key_press)
        self.root.bind("R", self.on_key_press)
        
        # Create info frame
        self.info_frame = tk.Frame(root, bg="gray20")
        self.info_frame.pack(fill=tk.X)
        
        self.score_label = tk.Label(
            self.info_frame,
            text=f"Score: {self.score}",
            font=("Arial", 14),
            bg="gray20",
            fg="white"
        )
        self.score_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.status_label = tk.Label(
            self.info_frame,
            text="Press SPACE to pause | Arrow keys to move",
            font=("Arial", 10),
            bg="gray20",
            fg="yellow"
        )
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Start game loop
        self.game_loop()
    
    def spawn_food(self):
        """Spawn food at a random location not occupied by snake"""
        while True:
            x = random.randint(0, self.GRID_WIDTH - 1)
            y = random.randint(0, self.GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.keysym
        
        if key == "Up" and self.direction != (0, 1):
            self.next_direction = (0, -1)
        elif key == "Down" and self.direction != (0, -1):
            self.next_direction = (0, 1)
        elif key == "Left" and self.direction != (1, 0):
            self.next_direction = (-1, 0)
        elif key == "Right" and self.direction != (-1, 0):
            self.next_direction = (1, 0)
        elif key == "space":
            self.paused = not self.paused
            if self.paused:
                self.status_label.config(text="PAUSED - Press SPACE to resume")
            else:
                self.status_label.config(text="Press SPACE to pause | Arrow keys to move")
        elif (key == "r" or key == "R") and self.game_over:
            self.reset_game()
    
    def update_game(self):
        """Update game state"""
        if self.game_over or self.paused:
            return
        
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        
        new_head = (head_x + dx, head_y + dy)
        
        # Check collision with walls
        if (new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.end_game()
            return
        
        # Check collision with self
        if new_head in self.snake:
            self.end_game()
            return
        
        self.snake.appendleft(new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
            # Increase speed slightly
            if self.speed > 40:
                self.speed -= 1
        else:
            self.snake.pop()
        
        self.score_label.config(text=f"Score: {self.score}")
    
    def draw(self):
        """Draw game elements"""
        self.canvas.delete("all")
        
        # Draw grid (optional)
        # for i in range(0, self.WINDOW_WIDTH, self.GRID_SIZE):
        #     self.canvas.create_line(i, 0, i, self.WINDOW_HEIGHT, fill="gray10")
        # for i in range(0, self.WINDOW_HEIGHT, self.GRID_SIZE):
        #     self.canvas.create_line(0, i, self.WINDOW_WIDTH, i, fill="gray10")
        
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            color = "lime" if i == 0 else "green"
            self.canvas.create_rectangle(
                x * self.GRID_SIZE,
                y * self.GRID_SIZE,
                x * self.GRID_SIZE + self.GRID_SIZE - 1,
                y * self.GRID_SIZE + self.GRID_SIZE - 1,
                fill=color,
                outline="darkgreen"
            )
        
        # Draw food
        food_x, food_y = self.food
        self.canvas.create_rectangle(
            food_x * self.GRID_SIZE,
            food_y * self.GRID_SIZE,
            food_x * self.GRID_SIZE + self.GRID_SIZE - 1,
            food_y * self.GRID_SIZE + self.GRID_SIZE - 1,
            fill="red",
            outline="darkred"
        )
        
        # Draw game over message
        if self.game_over:
            self.canvas.create_text(
                self.WINDOW_WIDTH // 2,
                self.WINDOW_HEIGHT // 2,
                text="GAME OVER",
                font=("Arial", 40, "bold"),
                fill="red"
            )
            self.canvas.create_text(
                self.WINDOW_WIDTH // 2,
                self.WINDOW_HEIGHT // 2 + 50,
                text=f"Final Score: {self.score}",
                font=("Arial", 24),
                fill="yellow"
            )
            self.canvas.create_text(
                self.WINDOW_WIDTH // 2,
                self.WINDOW_HEIGHT // 2 + 100,
                text="Press 'R' to restart",
                font=("Arial", 16),
                fill="white"
            )
    
    def end_game(self):
        """End the game"""
        self.game_over = True
        self.status_label.config(text="Game Over! Press 'R' to restart")
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.snake = deque([(self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2)])
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        self.paused = False
        self.speed = 100
        self.status_label.config(text="Press SPACE to pause | Arrow keys to move")
    
    def game_loop(self):
        """Main game loop"""
        self.update_game()
        self.draw()
        self.root.after(self.speed, self.game_loop)


def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
