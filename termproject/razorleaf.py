
import random
from pico2d import *
import gfw
import gobj
import math


class RazorLeaf:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    #뒤에있는 숫자는 이미지파일의 시작 인덱스이다.
    STATES = {'Ready':0,'Fire':9}
    #돌에대한 이미지만 받을것이기떄문에 dic이 아닌 list
    images = []
    FPS = {'Ready':8,'Fire':1}
    LASER_INTERVAL = 0

    #constructor
    def __init__(self,image,state):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 500,300
        self.delta = 0,0
        self.speed = 2
        self.gravity = 10
        self.time = 0
        self.width = 10
        self.height = 10
        self.dtheta = 0
        self.shaketime = 0
        self.state = state
        RazorLeaf.images = image

    def draw(self,posi):
        image = RazorLeaf.images[RazorLeaf.STATES[self.state]]
        image.draw(*self.pos)
        
             


    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        dy -= self.gravity
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        if y <-10 or x < -5:
            self.remove()


        self.pos = x,y
        self.delta = dx,dy

    def screenshake(self,pos):
        # self.shaketime += gfw.delta_time
        # if 0 < self.shaketime and self.shaketime < 0.2: 
        #     pos1 =(math.sin(self.dtheta*180/math.pi) * 5, math.sin(self.dtheta*180/math.pi) * 5)
        #     pos[0] = pos1
        #     self.dtheta = (self.dtheta+1) % 360
        # if self.shaketime > 1:
        #     self.shaketime = 0
        pass


    def remove(self):
        #print((Bullet.bullets))
        gfw.world.remove(self)
        #print(Bullet.bullets)
        
    



    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)        
