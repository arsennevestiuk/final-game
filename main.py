from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall
from random import randint
from time import sleep

tiles = 2 
scroll = 0
a = 400

window = display.set_mode((900,500))
WINDOW_WIDTH, WINDOW_HEIGHT = display.get_surface().get_size()
bg = transform.scale(image.load("bg.png"), (WINDOW_WIDTH,WINDOW_HEIGHT))
bg_width = bg.get_width()
bg_height = bg.get_height()

game = True
run = True
clock = time.Clock()

btn1 = Button('start_btn.png', 450 ,100, 100, 50)
btn2 = Button('exit_btn.png', 300,100, 100, 50)

player = Player('mario_standing.png','mario_right.png', int(WINDOW_HEIGHT/10),int(WINDOW_WIDTH/10) , 100,200)
money1 = GameSprite('pngwing.com.png',50,50 , 400,50)
money2 = GameSprite('pngwing.com.png',50,50 , 0,250)
money3 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money4 = GameSprite('pngwing.com.png',50,50 , 2000,50)
money5 = GameSprite('pngwing.com.png',50,50 , 2000,250)
money6 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money7 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money8 = GameSprite('pngwing.com.png',50,50 , 2000,250)
money9 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money10 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money11 = GameSprite('pngwing.com.png',50,50 , 2000,50)
money12 = GameSprite('pngwing.com.png',50,50 , 2000,250)
money13 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money14 = GameSprite('pngwing.com.png',50,50 , 2000,50)
money15 = GameSprite('pngwing.com.png',50,50 , 2000,250)
money16 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money17 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money18 = GameSprite('pngwing.com.png',50,50 , 2000,250)
money19 = GameSprite('pngwing.com.png',50,50 , 2000,380)
money20 = GameSprite('pngwing.com.png',50,50 , 2000,380)
priz = GameSprite('nefr.jpg',50,50, 2000,380)
priz1 = GameSprite('nefr.jpg',50,50, 0,50)
piy = GameSprite('piy.png',15,15, 1000, 200)
piy1 = GameSprite('piy.png',15,15, 1000, 45)
shipi = GameSprite('shipi.png',100,50,400,400)
shipi1 = GameSprite('shipi.png',100,50,500,400)
shipi2 = GameSprite('shipi.png',100,50,600,400)
teleport = GameSprite('teleport.png',50,50,850,390)
teleport1 = GameSprite('teleport.png',50,50,850,390)
monster = GameSprite('monster.png',50,50,5000,380)
key = GameSprite('key.png',50,50,2000,10)
chest = GameSprite('chest.png',50,50,2000,20)
wall1 = Wall(100,30,100,400,(255,0,0))
wall2 = Wall(100,30,0,300,(255,0,0))
wall3 = Wall(100,30,200,150,(255,0,0))
wall4 = Wall(100,30,400,100,(255,0,0))
wall5 = Wall(100,30,500,250,(255,0,0))
wall6 = Wall(100,30,400,100,(255,0,0))
wall7 = Wall(100,30,2000,100,(255,0,0))
wall8 = Wall(100,30,2000,100,(255,0,0))
wall9 = Wall(100,30,2000,100,(255,0,0))


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
        
        if player.rect.colliderect(wall7.rect):
            player.rect.bottom = wall7.rect.top

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
        
        if player.rect.colliderect(money4.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money4.rect.x = 2000
        
        if player.rect.colliderect(money5.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money5.rect.x = 2000
        
        if player.rect.colliderect(money6.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money6.rect.x = 2000
        
        if player.rect.colliderect(money7.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money7.rect.x = 2000
        
        if player.rect.colliderect(money8.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money8.rect.x = 2000
        
        if player.rect.colliderect(money9.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money9.rect.x = 2000
        
        if player.rect.colliderect(money10.rect):
            count = count + 1
            img = font1.render(str(count),True,(255,255,255))
            money10.rect.x = 2000

        if player.rect.colliderect(shipi.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))
        
        if player.rect.colliderect(shipi1.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))
        
        if player.rect.colliderect(shipi2.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))
        
        if player.rect.colliderect(piy.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))
        
        if player.rect.colliderect(piy1.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))
        
        if player.rect.colliderect(monster.rect):
            life = life - 1
            img2 = font2.render(str(life),True,(255,0,0))

        if player.rect.colliderect(key.rect):
                wall6 = Wall(100,20,800,100,(255,0,0))
                key.rect.x = 2000

        if player.rect.colliderect(priz.rect):
            priz = GameSprite('nefr.jpg',50,50, 2000,380)
            money6 = GameSprite('pngwing.com.png',50,50 , 800,0)
        
        if player.rect.colliderect(priz1.rect):
            priz1 = GameSprite('nefr.jpg',50,50, 2000,380)
            money7 = GameSprite('pngwing.com.png',50,50 , 0,200)

        if player.rect.colliderect(chest.rect):
            count = count + 30
            img = font1.render(str(count),True,(255,255,255))
            wall1 = Wall(100,30,2000,300,(255,0,0))
            wall2 = Wall(100,30,2000,200,(255,0,0))
            wall3 = Wall(100,30,2000,150,(255,0,0))
            wall4 = Wall(30,100,2000,100,(255,0,0))
            wall5 = Wall(100,30,2000,100,(255,0,0))
            wall6 = Wall(100,30,2000,100,(255,0,0))
            wall7 = Wall(100,30,2000,200,(255,0,0))
            wall8 = Wall(30,100,2000,100,(255,0,0))
            wall9 = Wall(30,100,2000,100,(255,0,0))
            money1 = GameSprite('pngwing.com.png',50,50 , 100,380)
            money2 = GameSprite('pngwing.com.png',50,50 , 150,380)
            money3 = GameSprite('pngwing.com.png',50,50 , 200,380)
            money4 = GameSprite('pngwing.com.png',50,50 , 250,380)
            money5 = GameSprite('pngwing.com.png',50,50 , 300,380)
            money6 = GameSprite('pngwing.com.png',50,50 , 350,380)
            money7 = GameSprite('pngwing.com.png',50,50 , 400,380)
            money8 = GameSprite('pngwing.com.png',50,50 , 450,380)
            money9 = GameSprite('pngwing.com.png',50,50 , 500,380)
            money10 = GameSprite('pngwing.com.png',50,50 , 550,330)
            money11 = GameSprite('pngwing.com.png',50,50 , 100,330)
            money12 = GameSprite('pngwing.com.png',50,50 , 150,330)
            money13 = GameSprite('pngwing.com.png',50,50 , 200,330)
            money14 = GameSprite('pngwing.com.png',50,50 , 250,330)
            money15 = GameSprite('pngwing.com.png',50,50 , 300,330)
            money16 = GameSprite('pngwing.com.png',50,50 , 350,330)
            money17 = GameSprite('pngwing.com.png',50,50 , 400,330)
            money18 = GameSprite('pngwing.com.png',50,50 , 450,330)
            money19 = GameSprite('pngwing.com.png',50,50 , 500,330)
            money20 = GameSprite('pngwing.com.png',50,50 , 550,330)
            teleport1 = GameSprite('teleport.png',50,50,2000,390)
            chest = GameSprite('chest.png',50,50,2000,20)
            shipi = GameSprite('shipi.png',100,50,2000,400)
            shipi1 = GameSprite('shipi.png',100,50,2000,400)
            shipi2 = GameSprite('shipi.png',100,50,2000,400)
            piy = GameSprite('piy.png',15,15, 100000, 200)
            piy1 = GameSprite('piy.png',15,15, 100000, 45)
            monster = GameSprite('monster.png',50,50,5000,380)


        if player.rect.colliderect(teleport.rect):
            wall1 = Wall(100,30,800,300,(255,0,0))
            wall2 = Wall(100,30,650,200,(255,0,0))
            wall3 = Wall(100,30,350,150,(255,0,0))
            wall4 = Wall(30,100,600,100,(255,0,0))
            wall5 = Wall(100,30,550,100,(255,0,0))
            wall6 = Wall(100,30,500,100,(255,0,0))
            wall7 = Wall(100,30,100,200,(255,0,0))
            wall8 = Wall(30,100,200,100,(255,0,0))
            wall9 = Wall(30,100,80,100,(255,0,0))

            money4 = GameSprite('pngwing.com.png',50,50 , 700,50)
            money5 = GameSprite('pngwing.com.png',50,50 , 800,250)
            money6 = GameSprite('pngwing.com.png',50,50 , 200,380)
            money7 = GameSprite('pngwing.com.png',50,50 , 120,100)
            teleport1 = GameSprite('teleport.png',50,50,10,380)
            monster = GameSprite('monster.png',50,50,50,380)
            priz = GameSprite('nefr.jpg',50,50, 800,50)

        if player.rect.colliderect(teleport1.rect):
            a = 800
            money1 = GameSprite('pngwing.com.png',50,50 , 700,180)
            money2 = GameSprite('pngwing.com.png',50,50 , 750,380)
            money3 = GameSprite('pngwing.com.png',50,50 , 250,330)
            money4 = GameSprite('pngwing.com.png',50,50 , 550,200)
            wall1 = Wall(30,100,100,250,(255,0,0))
            wall2 = Wall(100,30,650,200,(255,0,0))
            wall3 = Wall(100,30,350,150,(255,0,0))
            wall4 = Wall(30,100,800,0,(255,255,255))
            wall5 = Wall(100,30,550,250,(255,0,0))
            wall7 = Wall(100,30,100,200,(255,0,0))
            wall8 = Wall(30,100,2000,100,(255,0,0))
            wall9 = Wall(30,100,2000,100,(255,0,0))


            key = GameSprite('key.png',50,50,800,380)
            teleport = GameSprite('teleport.png',50,50,2000,390)
            monster = GameSprite('monster.png',50,50,800,380)
            chest = GameSprite('chest.png',50,50,830,10)

        if abs(scroll) > bg_width:
            scroll = 0
            

        scroll -= 5
        wall1.draw_wall(window)
        wall2.draw_wall(window)
        wall3.draw_wall(window)
        wall4.draw_wall(window)
        wall5.draw_wall(window)
        wall6.draw_wall(window)
        wall7.draw_wall(window)
        wall8.draw_wall(window)
        wall9.draw_wall(window)
        

        money1.draw(window)
        money2.draw(window)
        money3.draw(window)
        money4.draw(window)
        money5.draw(window)
        money6.draw(window)
        money7.draw(window)
        money8.draw(window)
        money9.draw(window)
        money10.draw(window)
        money11.draw(window)
        money12.draw(window)
        money13.draw(window)
        money14.draw(window)
        money15.draw(window)
        money16.draw(window)
        money17.draw(window)
        money18.draw(window)
        money19.draw(window)
        money20.draw(window)

        priz.draw(window)
        priz1.draw(window)

        shipi.draw(window)
        shipi1.draw(window)
        shipi2.draw(window)

        piy.rect.x-=3
        if piy.rect.x < 0:
            piy.rect.x = 700
        piy.draw(window)
        piy1.rect.x-=1
        if piy1.rect.x < 0:
            piy1.rect.x = 700
        piy1.draw(window)


        teleport.draw(window) 
        teleport1.draw(window)
        
        monster.draw(window)
        monster.rect.x-= 1
        if monster.rect.x < 0:
            monster.rect.x = a
        
        key.draw(window)

        chest.draw(window)

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
    clock.tick(60)
