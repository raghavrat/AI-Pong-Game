# AI Pong Game

A classic Pong game implementation with an AI opponent using Pygame. Play against a computer-controlled paddle that predicts ball movement with realistic error margins.

## Game Features

### Player Paddle
```python
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
        self.score = 0
```
- Controlled using up/down arrow keys
- Smooth movement with collision detection
- Score tracking

### AI Opponent
```python
def ai_move(self, ball):
    prediction_error = random.randint(-20, 20)
    target_y = ball.rect.centery + prediction_error
```
- Tracks ball movement
- Realistic prediction with random error
- Smooth paddle movement
- Adaptive difficulty through prediction errors

### Ball Physics
```python
class Ball:
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1
```
- Dynamic ball movement
- Wall and paddle collision detection
- Random starting direction
- Speed adjustments on collisions

## Controls

- **Up Arrow**: Move player paddle up
- **Down Arrow**: Move player paddle down
- **Close Window**: Exit game
## Game Mechanics

### Scoring System
```python
if ball.rect.left <= 0:
    ai.score += 1
    ball.reset()
elif ball.rect.right >= WINDOW_WIDTH:
    player.score += 1
    ball.reset()
```
- Points awarded when ball passes opponent's paddle
- Score display at top of screen
- Ball resets after each point

### AI Behavior
- Predicts ball trajectory
- Includes randomized error for realistic gameplay
- Smooth movement towards predicted position
- Speed-limited for fair gameplay

### Visual Elements
- Clean, classic Pong aesthetic
- Center line divider
- Score display
- White paddles and ball on black background

## Code Structure

### Main Components

1. **Paddle Class**
```python
class Paddle:
    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        elif not up and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed
```
- Handles paddle movement
- Manages collision boundaries
- Tracks individual scores

2. **Ball Class**
```python
class Ball:
    def reset(self):
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])
```
- Controls ball movement
- Handles collision response
- Manages reset functionality

3. **Game Loop**
```python
def main():
    while running:
        # Handle events
        # Update game state
        # Draw elements
        clock.tick(60)
```
- Event handling
- State updates
- Rendering
- Frame rate control

## Requirements

- Python 3.x
- Pygame library
- `constants.py` file with game constants

## Customization

You can modify these values in `constants.py`:
- `WINDOW_WIDTH`: Game window width
- `WINDOW_HEIGHT`: Game window height
- `PADDLE_WIDTH`: Width of paddles
- `PADDLE_HEIGHT`: Height of paddles
- `PADDLE_SPEED`: Movement speed of paddles
- `BALL_SIZE`: Size of the ball
- `BALL_SPEED`: Initial ball speed
- `WHITE`: Color for game elements
- `BLACK`: Background color



## Installation

1. Clone the Repository
```bash
git clone [repository-url]
cd ai-pong
```

2. Install Required Library
```bash
pip install pygame
```

3. Run the Game
```bash
python pong.py
```

