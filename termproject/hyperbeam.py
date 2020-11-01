
import random
from pico2d import *
import gfw
import gobj
import math


class HyperBeam:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    STATES = {'Beam':0,'Charge':5}
    #돌에대한 이미지만 받을것이기떄문에 dic이 아닌 list
    images = []
    FPS = {'Beam':5,'Charge':6}
    LASER_INTERVAL = 0

    #constructor
    def __init__(self,image,state):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 500,300
        self.delta = 1,0
        self.speed = 2
        self.gravity = 10
        self.time = 0
        self.width = 10
        self.height = 10
        self.dtheta = 0
        self.shaketime = 0
        self.Chargingtime = 3.5
        self.Firetime = 3.0
        self.dimgsize = 1.0
        self.fidx = 0
        self.state = state
        self.rad = 0
        HyperBeam.images = image

    def draw(self,posi):
        # if self.laser_time < Player.LASER_INTERVAL:
        #     self.state = 'Attack'
        # images = self.images[self.state]
        # image = images[self.fidx % len(images)]
        # result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
        # self.width = Player.IMAGESIZE[self.state][self.fidx%len(images)][0]       
        # self.height = Player.IMAGESIZE[self.state][self.fidx%len(images)][1]
        # image.composite_draw(0,self.flip,*result_posi)    
        image = HyperBeam.images[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]
        image.composite_draw(self.rad,'',*self.pos,image.w*self.dimgsize,image.h*self.dimgsize)
       #image.draw(*self.pos,100,100)
        
             


    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time*HyperBeam.FPS[self.state])
        if self.state == 'Charge':
            self.rad+=0.1
            self.dimgsize += 0.01
        if self.time > self.Chargingtime:
            self.state = 'Beam'
            self.pos = gobj.canv_width//2,gobj.canv_height//2
            self.dimgsize = 8.2
            self.rad = 0
        # x,y = self.pos
        # dx,dy = self.delta
        # dy -= self.gravity
        # x += dx * self.speed * gfw.delta_time
        # y += dy * self.speed * gfw.delta_time

        # if 60 < x and x < 280:
        #     if y - HyperBeam.images[HyperBeam.STATES[self.state]].h < 60 and dy < 0:
        #         dy *= -1
        #         Ldx = -20
        #         Rdx = 20
        #         if(self.state == 'Large'):
        #             rock = HyperBeam(HyperBeam.images, 'medium', x, y, Ldx, dy)
        #             gfw.world.add(gfw.layer.rock, rock)
        #             rock = HyperBeam(HyperBeam.images, 'medium', x, y, Rdx, dy)
        #             gfw.world.add(gfw.layer.rock, rock)
        #             self.remove()
        #         elif (self.state == 'medium'):
        #             rock = HyperBeam(HyperBeam.images, 'small', x, y, Ldx, dy)
        #             gfw.world.add(gfw.layer.rock, rock)
        #             rock = HyperBeam(HyperBeam.images, 'small', x, y, Rdx, dy)
        #             gfw.world.add(gfw.layer.rock, rock)
        #             self.remove()
        #         elif (self.state == 'small'):
        #             self.remove()
        # if y <-10:
        #     self.remove()


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
