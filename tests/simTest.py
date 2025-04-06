import pygame
import math

pygame.init()
pygame.joystick.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Helios Mk.I")

clock = pygame.time.Clock()

joystick = pygame.joystick.Joystick(0)
joystick.init()

font = pygame.font.SysFont(None, 30)

def draw_drone(x, y, yaw, throttle):
    size = 60
    color = (255, 215, 0)

    points = [
        (x + math.cos(yaw) * size, y + math.sin(yaw) * size),
        (x + math.cos(yaw + 2.5) * size / 1.5, y + math.sin(yaw + 2.5) * size / 1.5),
        (x + math.cos(yaw - 2.5) * size / 1.5, y + math.sin(yaw - 2.5) * size / 1.5),
    ]
    pygame.draw.polygon(screen, color, points)

def text(s, pos):
    img = font.render(s, True, (255, 255, 255))
    screen.blit(img, pos)

x, y = WIDTH // 2, HEIGHT // 2
yaw = 0

running = True
while running:
    screen.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.event.pump()

    throttle = -joystick.get_axis(1)
    pitch = joystick.get_axis(3)
    roll = joystick.get_axis(2)
    yaw_input = joystick.get_axis(0)

    # Movement
    x += roll * 5
    y += pitch * 5
    yaw += yaw_input * 0.05

    draw_drone(x, y, yaw, throttle)

    text(f"Throttle: {round(throttle, 2)}", (10, 10))
    text(f"Pitch: {round(pitch, 2)}", (10, 40))
    text(f"Roll: {round(roll, 2)}", (10, 70))
    text(f"Yaw: {round(yaw_input, 2)}", (10, 100))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
