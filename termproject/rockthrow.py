
import random
from pico2d import *
import gfw
import gobj
import math


class RockThrow:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    STATES = {'Large':0,'medium':1,'small':2}
    #돌에대한 이미지만 받을것이기떄문에 dic이 아닌 list
    images = []
    FPS = {'Pattern1':1,'Pattern2':1,'Pattern3':1}
    LASER_INTERVAL = 0

    #constructor
    def __init__(self,image,state,x,y,dx,dy):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = x,y
        self.delta = dx,dy
        self.speed = 2
        self.gravity = 10
        self.time = 0
        self.width = 10
        self.height = 10
        self.dtheta = 0
        self.shaketime = 0
        self.state = state
        RockThrow.images = image

    def draw(self,posi):
        image = RockThrow.images[RockThrow.STATES[self.state]]
        image.draw(*self.pos)
        
             


    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        dy -= self.gravity
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        if 60 < x and x < 280:
            if y - RockThrow.images[RockThrow.STATES[self.state]].h < 60 and dy < 0:
                dy *= -1
                Ldx = -20
                Rdx = 20
                if(self.state == 'Large'):
                    rock = RockThrow(RockThrow.images, 'medium', x, y, Ldx, dy)
                    gfw.world.add(gfw.layer.rock, rock)
                    rock = RockThrow(RockThrow.images, 'medium', x, y, Rdx, dy)
                    gfw.world.add(gfw.layer.rock, rock)
                    self.remove()
                elif (self.state == 'medium'):
                    rock = RockThrow(RockThrow.images, 'small', x, y, Ldx, dy)
                    gfw.world.add(gfw.layer.rock, rock)
                    rock = RockThrow(RockThrow.images, 'small', x, y, Rdx, dy)
                    gfw.world.add(gfw.layer.rock, rock)
                    self.remove()
                elif (self.state == 'small'):
                    self.remove()
        if y <-10:
            self.remove()


        self.pos = x,y
        self.delta = dx,dy

    def screenshake(self,pos):
        self.shaketime += gfw.delta_time
        if 0 < self.shaketime and self.shaketime < 0.2: 
            pos1 =(math.sin(self.dtheta*180/math.pi) * 5, math.sin(self.dtheta*180/math.pi) * 5)
            pos[0] = pos1
            self.dtheta = (self.dtheta+1) % 360
        if self.shaketime > 1:
            self.shaketime = 0


    def remove(self):
        #print((Bullet.bullets))
        gfw.world.remove(self)
        #print(Bullet.bullets)
        
    



    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)        
