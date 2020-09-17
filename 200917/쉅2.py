import random
from pico2d import *


class Boy:
    def __init__(self):#생성자
        #self.x, self.y = get_canvas_width() // 2, 85
        self.x,self.y = random.randint(100,700),random.randint(100,500)
        self.image=load_image('../res/run_animation.png')
        self.dx = random.random()
        self.frame = random.randint(0,7)
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
        
print("hi")
print(__name__)
