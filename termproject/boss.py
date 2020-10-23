
import random
from pico2d import *
import gfw
import gobj

class Boss:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    STATES = ['Attack','Idle' ,'Walk' ,'Jump','Double_jump','Fall']
    images = {}
    FPS = 1
    LASER_INTERVAL = 0

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 300, 300
        self.delta = (0, 0)
        self.speed = 200
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
        self.images = Boss.load_images()
        self.state = 'Idle'
        self.wh = ()
        self.width = 10
        self.height = 10
        self.flip = ''
        self.laser_time = 0
        self.bulletnum = 0
        self.gravity = 0.1

    @staticmethod
    def load_images():
        images = {}
        count = 0
        state_value = 0
        file_fmt = '%s/보스/3827.png'
        state_images = []
        fn = file_fmt % (gobj.RES_DIR)
        if os.path.isfile(fn):
            state_images.append(gfw.image.load(fn))
        images[0] = state_images
        return images



 

    def draw(self,posi):
        images = self.images[0]
        image = images[self.fidx % len(images)]
        result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
        image.composite_draw(0,self.flip,*result_posi,85,200)
       # image.composite_draw(0,self.flip,*result_posi,self.width,self.height)
            

    def update(self):
      
            



        # self.pos = x,y
        # self.delta = dx,dy
        # self.time += gfw.delta_time
        self.fidx = round(self.time*Boss.FPS)
        


    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)        

