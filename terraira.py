from turtledemo.lindenmayer import draw

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class Player:
    def __init__(self, x = 200, y = 100):
        self.head = pygame.Rect(x, y-90, 30, 30)
        self.body = pygame.Rect(x-5, y-60, 40, 60)
        self.legs = pygame.Rect(x, y, 30, 40)
        self.speed = 10

    def draw(self):
        pygame.draw.rect(window, (201, 197, 177), self.head)
        pygame.draw.rect(window, (32, 138, 250), self.body)
        pygame.draw.rect(window, (2, 26, 51), self.legs)


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.head.x -= self.speed
            self.body.x -= self.speed
            self.legs.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.head.x += self.speed
            self.body.x += self.speed
            self.legs.x += self.speed

class Block:
    def __init__(self, x, y, color, type):
        self.type = type
        self.color = color
        self.rect = pygame.Rect(x, y, 60, 60)

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, (0, 0, 0), self.rect,1)

block = Block(300,200, (39, 168, 73), "Grass")

player = Player(400, 200)
player2 = Player()

world = []
for i in range(27):
    world.append(Block(i*60,360, (39, 168, 73), "Grass"))

for i in range(27):
    world.append(Block(i * 60, 420, (165, 42, 42), "Dirt"))

for i in range(27):
    world.append(Block(i * 60, 480, (165, 42, 42), "Dirt"))

for i in range(27):
    world.append(Block(i * 60, 540, (89, 89, 89), "Stone"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.move()
    window.fill((138, 210, 255))
    player.draw()
    player2.draw()
    for block in world:
        block.draw()
    pygame.display.update()
    clock.tick(60)