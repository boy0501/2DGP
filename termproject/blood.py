import random
from pico2d import *
import gfw
import gobj

class Blood:
    #image = gfw.image.load(gobj.RES_DIR + '/2862.png')
    FPS = 1
    # FCOUNT = 10
    bloods = []
    BLOOD_MAX = 5
    BLOOD_NUM = 0  #현재 총알갯수


    def __init__(self,pos,dx,dy):
        # if len(Blood.images) == 0:
        #     self.load_images('male')
        #     self.load_images('female')

        self.pos = pos
        self.delta = 1 * dx, 1 * dy
        self.for_get_bb_pos = 0,0
        self.image = gfw.image.load(gobj.RES_DIR + '/2862.png')
        self.speed = 500
        self.fidx = 0
        self.time = 0

    def get_bb(self):
        x,y = self.for_get_bb_pos
        return x - 4, y - 3, x + 4, y + 3

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Blood.FPS)
        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        #y += dy * self.speed * gfw.delta_time
        self.pos = x,y
        if((self.pos[0] > get_canvas_width()+8 )|(self.pos[0] < -8)):
            self.remove()
    
    def screenshake(self,pos):
        pass       
        
    def draw(self,pos):
        image = self.image
        flip = 'h' if self.delta[0] < 0 else ''
        result_posi = (self.pos[0] + pos[0],self.pos[1]+pos[1])
        self.for_get_bb_pos = result_posi
        image.composite_draw(0, flip, *result_posi, 8, 6)

    def remove(self):
        #print((Blood.bloods))
        gfw.world.remove(self)
        Blood.BLOOD_NUM -= 1
        #print(Blood.bloods)
