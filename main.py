from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall
from random import randint

tiles = 2 
scroll = 0

window = display.set_mode((900,500))
WINDOW_WIDTH, WINDOW_HEIGHT = display.get_surface().get_size()
bg = transform.scale(image.load("bg.png"), (WINDOW_WIDTH,WINDOW_HEIGHT))
bg_width = bg.get_width()
bg_height = bg.get_height()

game = True
run = True
clock = time.Clock()

btn1 = Button('start_btn.png',  int(WINDOW_HEIGHT/2),int(WINDOW_WIDTH/2), 100, 50)
btn2 = Button('exit_btn.png', 300,100, 100, 50)

player = Player('mario_standing.png','mario_right.png', int(WINDOW_HEIGHT/10),int(WINDOW_WIDTH/10) , 100,200)
money1 = GameSprite('pngwing.com.png',50,50 , 400,50)
money2 = GameSprite('pngwing.com.png',50,50 , 0,250)
money3 = GameSprite('pngwing.com.png',50,50 , 700,380)
shipi = GameSprite('shipi.png',100,50,400,400)
shipi1 = GameSprite('shipi.png',100,50,500,400)
shipi2 = GameSprite('shipi.png',100,50,600,400)
wall1 = Wall(100,20,100,400,(255,0,0))
wall2 = Wall(100,20,0,300,(255,0,0))
wall3 = Wall(100,20,200,150,(255,0,0))
wall4 = Wall(100,20,400,100,(255,0,0))
wall5 = Wall(100,20,500,250,(255,0,0))
wall6 = Wall(100,20,400,100,(255,0,0))

speed = 0

ground = Wall(WINDOW_WIDTH, 70, 0, WINDOW_HEIGHT-70, color=(0,2,20))

bullets = []
walls = []
for i in range(3):
    wall = Wall(100,10, randint(650,1500),randint(100, 400), color=(255,0,0))
    walls.append(wall)

font.init()
font1 = font.SysFont("Arial",20)
font2 = font.SysFont("Arial",20)
count = 0
life = 1

img = font1.render(str(count),True,(255,255,255))
img2 = font2.render(str(life),True,(255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if life <= 0:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_LEFT:
                scroll -= 5
            if e.key == K_SPACE:
                player.isJump = True
            if e.key == K_RSHIFT:
                bullets.append(player.fire())
  
    if run:
        
        for i in range(0, tiles):
            window.blit(bg, (i * bg_width + scroll, 0))
        
        window.blit(img, (20,20))
        window.blit(img2, (850,20))
        
        player.rect.y += 3.2
        if player.rect.colliderect(wall1.rect):
            player.rect.bottom = wall1.rect.top

        if player.rect.colliderect(wall2.rect):
            player.rect.bottom = wall2.rect.top
        
        if player.rect.colliderect(wall3.rect):
            player.rect.bottom = wall3.rect.top

        if player.rect.colliderect(wall4.rect):
            player.rect.bottom = wall4.rect.top

        if player.rect.colliderect(wall5.rect):
            player.rect.bottom = wall5.rect.top

        if player.rect.colliderect(wall6.rect):
            player.rect.bottom = wall6.rect.top
        
        if player.rect.colliderect(money1.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money1.rect.x = 2000
        
        if player.rect.colliderect(money2.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money2.rect.x = 2000
        
        if player.rect.colliderect(money3.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money3.rect.x = 2000
        
        if player.rect.colliderect(shipi.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))
        
        if player.rect.colliderect(shipi1.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))
        
        if player.rect.colliderect(shipi2.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))


        if abs(scroll) > bg_width:
            scroll = 0
            

        scroll -= 5
        wall1.draw_wall(window)
        wall2.draw_wall(window)
        wall3.draw_wall(window)
        wall4.draw_wall(window)
        wall5.draw_wall(window)
        wall6.draw_wall(window)
        money1.draw(window)
        money2.draw(window)
        money3.draw(window)
        shipi.draw(window)
        shipi1.draw(window)
        shipi2.draw(window)
        player.draw(window)
        player.move()
        player.jump()
        player.rect.y += 3.2
        if player.rect.colliderect(ground.rect):
            player.rect.bottom = ground.rect.top
            

        ground.draw_wall(window)

        for b in bullets:
            b.update(window)
        

      
    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False
    
   
    display.update()
    clock.tick(120)
