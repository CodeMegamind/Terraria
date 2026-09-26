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
        self.velocity = 1

    def apply_gravity(self, blocks):
        self.head.y += self.velocity
        self.body.y += self.velocity
        self.legs.y += self.velocity
        self.velocity += 1

        for block in blocks:
            if block.rect.colliderect(self.legs):
                self.velocity = 0
                self.legs.bottom = block.rect.top
                self.body.bottom = self.legs.top
                self.head.bottom = self.body.top



    def draw(self, camera_x,camera_y):
        head_x = self.head.x - camera_x
        body_x = self.body.x - camera_x
        legs_x = self.legs.x - camera_x
        head_y = self.head.y - camera_y
        body_y = self.body.y - camera_y
        legs_y = self.legs.y - camera_y
        pygame.draw.rect(window, (201, 197, 177), (head_x, head_y, self.head.width, self.head.height))
        pygame.draw.rect(window, (32, 138, 250), (body_x, body_y, self.body.width, self.body.height))
        pygame.draw.rect(window, (2, 26, 51), (legs_x, legs_y, self.legs.width, self.legs.height))


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


    def draw(self, camera_x, camera_y):
        block_x = self.rect.x - camera_x
        block_y = self.rect.y - camera_y
        pygame.draw.rect(window, self.color, (block_x, block_y, self.rect.width, self.rect.height))
        pygame.draw.rect(window, (0, 0, 0), (block_x, block_y, self.rect.width, self.rect.height),1)




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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.velocity = -10

    player.move()
    player.apply_gravity(world)
    player2.apply_gravity(world)
    window.fill((138, 210, 255))
    camera_x = player.body.centerx - 400
    camera_y = player.body.centery - 400
    player.draw(camera_x, camera_y)
    player2.draw(camera_x, camera_y)
    for block in world:
        block.draw(camera_x, camera_y)
    pygame.display.update()
    clock.tick(60)