
import random
from pico2d import *
import gfw
import gobj


class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14
    }
    ACTIONS = ['Attack','Idle' ,'Walk' ,'Jump']
    ACTIONSDIC = {'Attack':14, 'Idle' : 0, 'Walk' :1 , 'Jump' : 7}
    IMAGESIZE ={'Walk':[(24,23),(16,25),(21,22),(16,25)],
                'Idle':[(32,32)],
                'Jump':[(32,32)],
                'Attack':[(32,32)]
    }
    images = {}
    FPS = 12

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 100, 100
        self.delta = 0, 0
        self.speed = 200
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
        self.images = Player.load_images()
        self.action = 'Idle'
        self.wh = ()
        self.width = 10
        self.height = 10
        self.flip = ''
       
    @staticmethod
    def load_images():
        images = {}
        count = 0
        action_value = 0
        file_fmt = '%s/Animation-%d Direction-%d Frame-%d.png'
        for action in Player.ACTIONS:
            action_images = []
            n = -1
            while True:
                n += 1
                action_value = Player.ACTIONSDIC[action]
                fn = file_fmt % (gobj.RES_DIR,action_value,0,n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        return images



    def fire(self):
        pass

    def draw(self,posi):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
        self.width = Player.IMAGESIZE[self.action][self.fidx%len(images)][0]       
        self.height = Player.IMAGESIZE[self.action][self.fidx%len(images)][1]
        image.composite_draw(0,self.flip,*result_posi,self.width,self.height)
        

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        print(dx,dy)        
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        self.pos = x,y
        self.time += gfw.delta_time
        self.fidx = round(self.time*Player.FPS)


    def handle_event(self, e):
        pair = (e.type, e.key)
        print(pair)
        if pair in Player.KEY_MAP:
            pdx = self.delta[0]
            self.delta = gobj.point_add(self.delta, Player.KEY_MAP[pair])
            dx = self.delta[0]
            self.action = \
                'Idle' if dx == 0 else \
                'Walk' if dx < 0 else \
                'Walk' if dx > 0 else \
                'Jump' 
            if dx == -1 :
                self.flip = 'h'
            elif dx == 1: 
                self.flip = ''
        if pair in Player.SPECIAL_KEY_MAP:
            self.action = \
                'Jump' if Player.SPECIAL_KEY_MAP[pair] == 7 else \
                'Attack'
            # print(dx, pdx, self.action)
            