
import random
from pico2d import *
import gfw
import gobj
import math
import player


class RazorLeaf:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    #뒤에있는 숫자는 이미지파일의 시작 인덱스이다.
    STATES = {'Ready':0,'Fire':8}
    #돌에대한 이미지만 받을것이기떄문에 dic이 아닌 list
    images = []
    FPS = {'Ready':7,'Fire':1}
    LASER_INTERVAL = 0

    #constructor
    def __init__(self,image,state):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 500,300
        self.delta = 0,1
        self.for_get_bb_pos = self.pos
        self.destination = 500,300
        self.speed = 5
        self.gravity = 10
        self.time = 0
        self.width = 10
        self.height = 10
        self.dtheta = 0
        self.shaketime = 0
        self.state = state
        self.Scale = 2
        self.ready_time = 1.5   #나뭇잎이 발사 되기 전 ready 상태
        self.fire_state = 0
        RazorLeaf.images = image
        self.Leafdest()
        self.music = load_wav('./res/미싱노브금/boss/razorleap1.wav')
        self.music.set_volume(gfw.Volume-10)
        self.music.play()

    def draw(self,posi):
        result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
        self.for_get_bb_pos = result_posi
        image = RazorLeaf.images[RazorLeaf.STATES[self.state] + self.fidx % RazorLeaf.FPS[self.state]]
        image.draw(*result_posi,image.w * self.Scale,image.h * self.Scale)
    
    def get_bb(self):
        image = RazorLeaf.images[RazorLeaf.STATES[self.state] + self.fidx % RazorLeaf.FPS[self.state]]
        x,y = self.for_get_bb_pos
        return x - image.w* self.Scale//2, y - image.h* self.Scale//2, x + image.w* self.Scale//2, y + image.h* self.Scale//2    
        
             
    def Leafdest(self):
        if self.state == 'Ready':
            self.destination = random.randint(400,550),random.randint(350,400)
            destx,desty = self.destination
            dx,dy = self.delta
            x,y = self.pos
            dx = (destx - x)/0.3
            dy = (desty - y)/0.3
            self.delta = dx,dy
        elif self.state =='Fire':
            self.destination = player.Player.PlayerPos
            destx,desty = self.destination
            dx,dy = self.delta
            x,y = self.pos
            dx = (destx - x)/1.7
            dy = (desty - y)/1.7
            self.delta = dx,dy

    def Leafmove(self,x,y,dx,dy):
        if x < self.destination[0]-2 or x >self.destination[0]+2:
            x += dx  * gfw.delta_time
        if y < self.destination[1]-2 or y >self.destination[1]+2:
            y += dy  * gfw.delta_time
        return x,y

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        if self.state == 'Fire':
            # dy -= self.gravity
            x += dx * self.speed * gfw.delta_time
            y += dy * self.speed * gfw.delta_time
        if self.state == 'Ready':
            x,y = self.Leafmove(x,y,dx,dy)

        self.time += gfw.delta_time
        self.fidx = round(self.time*RazorLeaf.FPS[self.state])

        if self.time > self.ready_time:
            self.state = 'Fire'
            if self.fire_state == 0:
                self.Leafdest()
                self.music = load_wav('./res/미싱노브금/boss/razorleap2.wav')
                self.music.set_volume(gfw.Volume-10)
                self.music.play()
                dx,dy = self.delta
                self.fire_state = 1

        if y <-10 or x < -5:
            self.remove()

            

        self.pos = x,y
        self.delta = dx,dy

    def screenshake(self,pos):
        if self.state == 'Fire':
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
