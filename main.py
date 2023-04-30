from pygame import *
from sprite import Player
from button import Button


window = display.set_mode((700,500))


game = True
run = False
clock = time.Clock()

btn1 = Button('start_btn.png', 250,100, 100, 50)
btn2 = Button('exit_btn.png',350,100,100,50)

player = Player("",30,70,100,200)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == K_ESCAPE:
            run = True

    if run:
        window.fill((200,10,20))
    else:
        window.fill((0,0,0))
        if btn2.draw(window):
            game = False
    

        if btn1.draw(window):
            run = True
    

   
    display.update()
    clock.tick(60)