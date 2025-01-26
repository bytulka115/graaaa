import random

import pygame

class Player:
    def __init__(self, speed, width, height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []
    def draw(self, window):
        window.blit(self.texture, self.hitbox)




def game():
    pygame.init()
    window = pygame.display.set_mode([700, 500])
    fps = pygame.time.Clock()
    player = Player(3, 65, 85, 147, 129, )


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



        pygame.display.flip()









    fps.tick(60)

game()