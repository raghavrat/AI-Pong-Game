import pygame
import random
from constants import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("AI Pong")


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
        self.score = 0

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        elif not up and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def ai_move(self, ball):
        prediction_error = random.randint(-20, 20)
        target_y = ball.rect.centery + prediction_error

        if self.rect.centery < target_y and self.rect.bottom < WINDOW_HEIGHT:
            self.move(False)
        elif self.rect.centery > target_y and self.rect.top > 0:
            self.move(True)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2,
                                WINDOW_HEIGHT // 2 - BALL_SIZE // 2,
                                BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED
        self.reset()

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def reset(self):
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])


def main():
    clock = pygame.time.Clock()

    player = Paddle(50, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ai = Paddle(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    font = pygame.font.Font(None, 74)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(True)
        if keys[pygame.K_DOWN]:
            player.move(False)

        ai.ai_move(ball)

        ball.move()

        if ball.rect.colliderect(player.rect) or ball.rect.colliderect(ai.rect):
            ball.speed_x *= -1

        if ball.rect.left <= 0:
            ai.score += 1
            ball.reset()
        elif ball.rect.right >= WINDOW_WIDTH:
            player.score += 1
            ball.reset()

        screen.fill(BLACK)
        player.draw()
        ai.draw()
        ball.draw()

        player_text = font.render(str(player.score), True, WHITE)
        ai_text = font.render(str(ai.score), True, WHITE)
        screen.blit(player_text, (WINDOW_WIDTH // 4, 20))
        screen.blit(ai_text, (3 * WINDOW_WIDTH // 4, 20))

        pygame.draw.aaline(screen, WHITE,
                           (WINDOW_WIDTH // 2, 0),
                           (WINDOW_WIDTH // 2, WINDOW_HEIGHT))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
