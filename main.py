import math
import random
import time

import pygame
from file_helper17 import *






class Player:
    def __init__(self, speed, width, height, x, y, skin, health=3):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.texture_right= self.texture
        self.texture_left = pygame.transform.flip(self.texture, True, False)
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []
        self.last_shoot = 0
        self.health = health

    def draw(self, window):
        window.blit(self.texture, self.hitbox)
        for bullet in self.bullets:
            bullet.draw(window)



    def move(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
            self.texture = self.texture_right

        if keys[pygame.K_f]:
            self.hitbox.y -= self.speed
            self.texture = self.texture_right


        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
            self.texture = self.texture_left
        if mouse[0]:
           data = read_from_file()
           if time.time()-self.last_shoot >data['gun']:
                target_x, target_y = pygame.mouse.get_pos()
                dx = target_x - self.hitbox.centerx
                dy = target_y - self.hitbox.centery
                self.angle = math.degrees(math.atan2(dy, dx))
                self.bullets.append(Bullet("gratis-png-bala-dorada-icono-de-bala-una-bala-thumbnail-removebg-preview.png",
                                        50, 30,
                                        self.hitbox.x, self.hitbox.y,
                                        9, self.angle))
                self.last_shoot= time.time()


        for bullet in self.bullets:
            bullet.update()






class Bullet:
    def __init__(self,  skin, width, height, x, y, speed, angle):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []
        self.angle = math.radians(angle)

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def move(self):
        self.hitbox.x -= self.speed

    def update(self):
        # Рух кулі в напрямку кута
        self.hitbox.x += self.speed * math.cos(self.angle)
        self.hitbox.y += self.speed * math.sin(self.angle)









class Enemy:
        def __init__(self, x, y, width, height, speed, skin):
            self.texture = pygame.image.load(skin)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.texture_right = self.texture
            self.texture_left = pygame.transform.flip(self.texture, True, False)
            self.hitbox = self.texture.get_rect()
            self.speed = speed
            self.hitbox.x = x
            self.hitbox.y = y



        def draw(self, window):
            window.blit(self.texture, self.hitbox)


        def move(self):
            self.hitbox.x += self.speed




def game():
    pygame.init()
    window = pygame.display.set_mode([700, 500])
    fps = pygame.time.Clock()
    data = read_from_file()
    player = Player(5, 65, 85, 147, 300, data['skin'])

    background = pygame.image.load("ORS97Z0.jpg")
    background = pygame.transform.scale(background, [700, 500])
    game = True

    num_enemies = 12
    enemies = []

    for i in range(5):
        enemies.append(Enemy(random.randint(-500, 0), 300, 65, 75, 4,"pngtree-green-robber-clip-art-png-image_2972817-removebg-preview.png" ))
        enemies.append(Enemy(random.randint(500, 1000), 300, 65, 75,  -4,
                             "pngtree-green-robber-clip-art-png-image_2972817-removebg-preview.png"))





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        window.fill([123, 123, 123])
        window.blit(background, [0, 0])


        for enemy in enemies:
            if enemy.hitbox.x>1000:
                enemy.hitbox.x = random.randint(-500, 0 )
            if enemy.hitbox.x<-1000:
                enemy.hitbox.x = random.randint(500, 1000 )







        if enemy.hitbox.colliderect(player.hitbox):
            player.health -= 1  # Subtract 1 from player's health when hit
            enemy.hitbox.x = random.randint(500, 1000)  # Reset enemy position after collision
            if player.health <= 0:
                print("Game Over!")
                pygame.quit()
                return  # Exit the game if health reaches 0







        for bullet in player.bullets[:]:
            for enemy in enemies[:]:
                if bullet.hitbox.colliderect(enemy.hitbox):
                    player.bullets.remove(bullet)  # Remove the bullet that hit the enemy
                    enemies.remove(enemy)  # Remove the enemy that was hit
                    break  # Exit the loop after one collision to avoid multiple removals


        window.fill([123, 123,  123])
        window.blit(background,[0, 0])



        player.move()
        player.draw(window)

        for enemy in enemies:
            enemy.draw(window)
            enemy.move()

        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Health: {player.health}", True, (255, 200, 0))
        window.blit(health_text, (10, 10))

        pygame.display.flip()







        fps.tick(60)

