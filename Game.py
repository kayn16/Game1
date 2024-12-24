import pygame
import random

# Display
pygame.init()
clock = pygame.time.Clock()
width = 500
height = 700
display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Midnight Racer")

# Music
pygame.mixer.music.load("Assets/music.mp3")
pygame.mixer.music.play(-1)

# Road
road_img = pygame.image.load("Assets/road.png")
road1 = [0,0]
road2 = [0, -height]

# Car
car_img = pygame.image.load("Assets/car.png")
car = car_img.get_rect(center=(width/2,600))
car_velx = 0
car_vely = 0

# Obstacle
obs_img = pygame.image.load("Assets/obstacle.png")
obs = obs_img.get_rect(center=(random.randint(80,width-80), random.randint(-1000,-500)))
obs_vel = 15

# Game Loop
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_velx = -10
            if event.key == pygame.K_RIGHT:
                car_velx = 10
            if event.key == pygame.K_UP:
                car_vely = -10
            if event.key == pygame.K_DOWN:
                car_vely = 10
        if event.type == pygame.KEYUP:
            car_velx = 0
            car_vely = 0

    # Car Movements
    car.x += car_velx
    car.y += car_vely

    if car.left <= 50:
        car.left = 50
    if car.right >= width-50:
        car.right = width-50
    if car.center[1] >= height:
        car.center = (car.center[0], height)
    if car.center[1] <= 0:
        car.center = (car.center[0], 0)

    # Road Movement
    road1[1] += 20
    road2[1] += 20

    if road1[1] >= height:
        road1[1] = -height
    if road2[1] >= height:
        road2[1] = -height

    # Obstacle Movement
    obs.y += obs_vel
    if obs.top >= height:
        obs.center = (random.randint(80,width-80), random.randint(-500,0))

    # Collision
    if car.colliderect(obs):
        game = False

    # Display Updates
    display.blit(road_img, road1)
    display.blit(road_img, road2)
    display.blit(car_img, car)
    display.blit(obs_img, obs)

    clock.tick(60)
    pygame.display.update()

pygame.quit()