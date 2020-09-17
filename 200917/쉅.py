#instantiation
#instance 클래스 만드는거

from pico2d import *
from random import randint as rint
from random import random as rfloat


class Boy:
    def __init__(self):#생성자
        #self.x, self.y = get_canvas_width() // 2, 85
        self.x,self.y = rint(100,700),rint(100,500)
        self.image=load_image('../res/run_animation.png')
        self.dx = rfloat()
        self.frame = rint(0,7)
    def draw(self):
         self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
    def update(self):
        self.x+=self.dx*5
        self.frame = (self.frame+1)%8
    
class Grass:
    def __init__(self):
        self.img = load_image('../res/grass.png')
        self.x,self.y=400,30
    def draw(self):
        self.img.draw(self.x,self.y)
        

def handle_events():
    global running, x, y, dx,boy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                boy.dx-=1
            elif e.key == SDLK_RIGHT:
                boy.dx +=1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
               boy.dx -= 1
        elif e.type == SDL_MOUSEMOTION:
            boy.x,boy.y = e.x,get_canvas_height() -e.y-1
                
            
open_canvas()

gra = load_image('../res/grass.png')

#boy = Boy()

team = [Boy() for i in range(11) ]

for b in team:
    b.x=rint(100,700)
    b.y=rint(100,700)

boy = team[0]

grass = Grass()
handle_events()
running = True
while running:
    clear_canvas()
    grass.draw()
    for b in team: b.draw()
    update_canvas()



    
    handle_events()
    for b in team: b.update()

    delay(0.01)

close_canvas()

