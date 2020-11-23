
import random
from pico2d import *
import gfw
import gobj
import math

class BossDieEffect:
    images = []
    FPS = 20
    #constructor
    def __init__(self,pos,images):
        self.pos = pos
        self.time = 0
        self.dtheta = random.randint(0,180)
        self.fidx = 0
        BossDieEffect.images = images

    def draw(self,posi):
        result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
        image = self.images[self.fidx % BossDieEffect.FPS]
        image.draw(*result_posi)

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time*BossDieEffect.FPS)
        if self.time > 0.5:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def screenshake(self,pos):
        pos1 =(math.sin(self.dtheta*180/math.pi) * 5, math.sin(self.dtheta*180/math.pi) * 5)
        pos[0] = pos1
        self.dtheta = (self.dtheta+1) % 360