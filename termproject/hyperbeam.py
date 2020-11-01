
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
    STATES = {'Beam':0,'Charge':5,'Energy':11}
    #돌에대한 이미지만 받을것이기떄문에 dic이 아닌 list
    images = []
    FPS = {'Beam':5,'Charge':6,'Energy':3}
    beampix = 16 * 7 #원본이미지에 8배 곱해준것
    BEAM = [(500-beampix/2,350-beampix/2),(500-beampix,350-beampix*3/4),(500-beampix*3/2,350-beampix),
    (500-beampix*39/16,350-beampix*25/16),(500-beampix*39/16,350-beampix*25/16)]
    LASER_INTERVAL = 0

    #constructor
    def __init__(self,image,state,x=500,y=300):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = x,y
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
        self.EnergyRe_gentime = 0.05
        self.Energytime = 0
        self.delaytime = 1.2
        self.dimgsize = 1.0
        self.fidx = 0
        self.beamtarget = 0,0
        self.state = state
        self.rad = 0
        self.radb = 0
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
        if self.time > self.delaytime or self.state!='Beam': 
            if(self.state == 'Beam'):
                self.pos = HyperBeam.BEAM[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]

            image = HyperBeam.images[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]
            image.composite_draw(self.rad,'',*self.pos,image.w*self.dimgsize,image.h*self.dimgsize)
       #image.draw(*self.pos,100,100)
        
             
    def EnergyMove(self):
        targetx = 500
        targety = 300
        x,y = self.pos
        dx = (targetx - x)/15
        dy = (targety - y)/15
        x += dx
        y += dy
        self.pos = x,y 

    def setBeamtuple(self):
        originalx = math.cos(0)
        originaly = math.sin(0)
        dx = math.cos(self.rad)
        dx = originalx - dx
        dy = math.sin(self.rad)
        dy = originaly - dy
        if (self.rad*180/math.pi) > 0:
            HyperBeam.BEAM = [
        (dx*HyperBeam.beampix +     500-HyperBeam.beampix/2 ,        dy*HyperBeam.beampix +             350-HyperBeam.beampix/2),
        (dx*HyperBeam.beampix*2 +   500-HyperBeam.beampix,           dy*HyperBeam.beampix*3/2 +          350-HyperBeam.beampix*3/4),
        (dx*HyperBeam.beampix*3 +   500-HyperBeam.beampix*3/2,       dy*HyperBeam.beampix*2 +           350-HyperBeam.beampix),
        (dx*HyperBeam.beampix*39/8 + 500-HyperBeam.beampix*39/16,    dy*HyperBeam.beampix*25/8   +     350-HyperBeam.beampix*25/16),
        (dx*HyperBeam.beampix*39/8 + 500-HyperBeam.beampix*39/16,    dy*HyperBeam.beampix*25/8    +    350-HyperBeam.beampix*25/16)]


    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time*HyperBeam.FPS[self.state])
        
        if self.state == 'Charge':
            self.rad+=0.1
            self.dimgsize += 0.01 
            self.Energytime += gfw.delta_time
            if self.Energytime > self.EnergyRe_gentime:
                self.Energytime = 0
                randomtheta = random.randint(0,360)
                randx = math.cos(randomtheta*180/math.pi)*150 +500
                randy = math.sin(randomtheta*180/math.pi)*150 +300
                energy = HyperBeam(HyperBeam.images, 'Energy', randx,randy)
                gfw.world.add(gfw.layer.beam, energy)
        if self.time > self.Chargingtime:
            self.time = 0
            self.state = 'Beam'
            self.pos = gobj.canv_width//2,gobj.canv_height//2
            self.dimgsize = 7
            #HyperBeam.beampix *= 7
            self.rad = 30 * math.pi / 180
            #self.rad = 0
            self.setBeamtuple()
        if self.state == 'Energy':
            self.EnergyMove()
            if self.pos[0]<510 and self.pos[0]>490:
                if self.pos[1]<310 and self.pos[1]>290:
                    self.remove()




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
