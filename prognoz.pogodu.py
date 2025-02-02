import math
import random
import time

import pygame







class Player:
    def __init__(self, speed, width, height, x, y, skin):
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

        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
            self.texture = self.texture_left
        if mouse[0]:
           if time.time()-self.last_shoot >0.5:
                target_x, target_y = pygame.mouse.get_pos()
                dx = target_x - self.hitbox.centerx
                dy = target_y - self.hitbox.centery
                self.angle = math.degrees(math.atan2(dy, dx))
                self.bullets.append(Bullet("gratis-png-bala-dorada-icono-de-bala-una-bala-thumbnail-removebg-preview.png",
                                        50, 30,
                                        self.hitbox.x, self.hitbox.y,
                                        3, self.angle))
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














def game():
    pygame.init()
    window = pygame.display.set_mode([700, 500])
    fps = pygame.time.Clock()
    player = Player(1, 65, 85, 147, 300, "Знімок_екрана_2025-01-26_142901-removebg-preview.png")


    background = pygame.image.load("ORS97Z0.jpg")
    background = pygame.transform.scale(background, [700, 500])
    game = True




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        window.fill([123, 123, 123])
        window.blit(background, [0, 0])





        window.fill([123, 123,  123])
        window.blit(background,[0, 0])



        player.move()
        player.draw(window)





        pygame.display.flip()







    fps.tick(60)

game()