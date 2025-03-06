import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Movement Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 5, 5

# Clock
clock = pygame.time.Clock()

# Main loop
def main():
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Bounce the ball off the walls
        if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
            ball_speed_x = -ball_speed_x
        if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
            ball_speed_y = -ball_speed_y

        # Drawing
        screen.fill(black)  # Clear the screen
        pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)  # Draw the ball
        pygame.display.flip()  # Update the display

        clock.tick(60)  # Limit the frame rate

if __name__ == "__main__":
    main()
