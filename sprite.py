from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,img_name,width,height,x,y):
        self.image = transform.scale(image.load(img_name),(width , height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, window):
        window.blit(self.image, (self.rect.x , self.rect.y))

class Player(GameSprite):
    def __init__(self,img_name,width,height,x,y):
        self.isJump = False
        self.jumpCount = 10


    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5
        if keys[K_SPACE]:
            isJump = True
    
    def jump(self):
        if self.isJump:
            self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10