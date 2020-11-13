
import random
from pico2d import *
import gfw
import gobj
import math
import bullet
import blood

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        #(SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        #(SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        #(SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        #(SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    STATES = ['Attack','Idle' ,'Walk' ,'Jump','Double_jump','Fall']
    STATESDIC = {'Attack':14, 'Idle' : 0, 'Walk' :1 , 'Jump' : 7,'Double_jump':7,'Fall' :7}
    IMAGESIZE ={'Walk':[(24,23),(16,25),(21,22),(16,25)],
                'Idle':[(32,32)],
                'Jump':[(32,32)],
                'Attack':[(32,32)],
                'Double_jump':[(32,32)],
                'Fall':[(32,32)]
    }
    IMAGESIZE_GETBB ={'Walk':[(24,23),(16,25),(21,22),(16,25)],
                'Idle':[(20,22)],
                'Jump':[(20,22)],
                'Attack':[(20,22)],
                'Double_jump':[(20,22)],
                'Fall':[(20,22)]
    }
    JUMP_STATES_DIC = {'Normal':0,'Jump':1,'Double_jump':2}
    images = {}
    FPS = 12
    LASER_INTERVAL = 0
    PlayerPos = 0,0

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 100, 100
        self.delta = (0, 0)
        self.for_get_bb_pos = 0,0
        self.speed = 200
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
        self.images = Player.load_images()
        self.state = 'Idle'
        self.wh = ()
        self.width = 10
        self.height = 10
        self.flip = ''
        self.laser_time = 0
        self.bulletnum = 0
        self.gravity = 0.1
        self.Djump_state = Player.JUMP_STATES_DIC['Normal']
        self.die_value = 0
        
        
    @staticmethod
    def load_images():
        images = {}
        count = 0
        state_value = 0
        file_fmt = '%s/Animation-%d Direction-%d Frame-%d.png'
        for state in Player.STATES:
            state_images = []
            n = -1
            while True:
                n += 1
                state_value = Player.STATESDIC[state]
                fn = file_fmt % (gobj.RES_DIR,state_value,0,n)
                if os.path.isfile(fn):
                    state_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[state] = state_images
        return images



    def get_bb(self):
        x,y = self.for_get_bb_pos
        if self.state == 'Walk':
            return x-self.width//2,y-self.height//2,x+self.width//2,y+self.height//2
        else:
            return x-11,y-16,x+11,y+9
        

    def draw(self,posi):
        #print(self.pos)
        if self.laser_time < Player.LASER_INTERVAL:
            self.state = 'Attack'
        images = self.images[self.state]
        image = images[self.fidx % len(images)]
        result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
        self.for_get_bb_pos = result_posi
        self.width = Player.IMAGESIZE_GETBB[self.state][self.fidx%len(images)][0]       
        self.height = Player.IMAGESIZE_GETBB[self.state][self.fidx%len(images)][1]
        image.composite_draw(0,self.flip,*result_posi)
        
       # image.composite_draw(0,self.flip,*result_posi,self.width,self.height)
        
    def jump(self):
        if self.state == 'Double_jump' or self.Djump_state == Player.JUMP_STATES_DIC['Double_jump']:
            return
        if self.state == 'Jump':
            self.state = 'Double_jump'
            self.Djump_state = Player.JUMP_STATES_DIC['Double_jump']
        elif self.state == 'Fall':
            self.state = 'Double_jump'
            self.Djump_state = Player.JUMP_STATES_DIC['Double_jump']
        else:
            self.state = 'Jump'
            self.Djump_state += 1
        deltay = 2.3
        deltax = self.delta[0]
        self.delta = deltax, deltay

    

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        #print(dx,dy)        

        dy -= self.gravity
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        if y <0:
            self.die()

        if 50<x and x <290:
            if y < 90 and dy < 0:
                dy = 0
                y = 90
                self.Djump_state = Player.JUMP_STATES_DIC['Normal']
        
        if self.state == 'Attack':
            self.laser_time += gfw.delta_time
            if self.laser_time >= Player.LASER_INTERVAL:
                self.laser_time = 0
                Player.LASER_INTERVAL = 0
                self.state = \
                'Jump' if dy != 0 and self.Djump_state == Player.JUMP_STATES_DIC['Normal'] else \
                'Double_jump' if dy != 0 and self.Djump_state == Player.JUMP_STATES_DIC['Jump'] else\
                'Idle' if dx == 0 else \
                'Walk' if dx < 0 else \
                'Walk' if dx > 0 else \
                'Idle'
        elif self.state in Player.STATES[-3:]:
            if y == 90 and dy ==0:
                if dx != 0:
                    self.state = 'Walk'
                else:
                    self.state = 'Idle'
            


        Player.PlayerPos = self.pos
        self.pos = x,y
        self.delta = dx,dy
        self.time += gfw.delta_time
        self.fidx = round(self.time*Player.FPS)
        

    def screenshake(self,pos):
        pass       
        
    def handle_event(self, e):
        pair = (e.type, e.key)
        #print(pair)
        if pair in Player.KEY_MAP:
            #pdx = self.delta[0]
            self.delta = gobj.point_add(self.delta, Player.KEY_MAP[pair])
            dx,dy = self.delta
            self.state = \
                'Jump' if dy != 0 else \
                'Idle' if dx == 0 else \
                'Walk' if dx < 0 else \
                'Walk' if dx > 0 else \
                'Jump'
            if dx == -1 :
                self.flip = 'h'
            elif dx == 1: 
                self.flip = ''
        if pair in Player.SPECIAL_KEY_MAP:
            if Player.SPECIAL_KEY_MAP[pair]==14:               
                self.state = 'Attack'
                self.fire()
            elif Player.SPECIAL_KEY_MAP[pair]==7:
                self.jump()
                  
            elif Player.SPECIAL_KEY_MAP[pair] == 8:
                dx,dy = self.delta
                if(dy>=0):
                    self.delta = (dx,0)

            # self.state = \
            #     'Jump' if Player.SPECIAL_KEY_MAP[pair] == 7 else \
            #     'Attack'
            #      gfw.world.add(gfw.layer.bullet, bullet)

            # print(dx, pdx, self.state)

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)    

    def die(self):
        for i in range(360):
            blood1 = blood.Blood(self.pos,math.cos(i * math.pi / 180)*100,math.sin(i * math.pi / 180)*100,random.randint(1,10))
            gfw.world.add(gfw.layer.blood,blood1)
        self.die_value = 1
        self.remove()
    
    def get_die_value(self):
        return self.die_value

    def fire(self):
        #print(len(bullet.Bullet.bullets))
        if(bullet.Bullet.BULLET_NUM<bullet.Bullet.BULLET_MAX):
            if self.flip == 'h':
                bullet1 = bullet.Bullet(self.pos[0]+4,self.pos[1]-4,-1)
            else:
                bullet1 = bullet.Bullet(self.pos[0]+4,self.pos[1]-4,1)
            gfw.world.add(gfw.layer.bullet,bullet1)
            bullet.Bullet.BULLET_NUM += 1
            Player.LASER_INTERVAL = 0.15   
        # if len(bullet.Bullet.bullets)<5:
        #     bullet1 = bullet.Bullet(*self.pos,200)
        #     #bullet.Bullet.bullets.append(bullet1)
        #     for b in range(0,len(bullet.Bullet.bullets)):
        #         gfw.world.add(gfw.layer.bullet,bullet.Bullet.bullets[b])
        #     Player.LASER_INTERVAL = 0.15
    def remove(self):
        gfw.world.remove(self)