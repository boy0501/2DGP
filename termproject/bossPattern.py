
import random
from pico2d import *
import gfw
import gobj
import math
import rockthrow
import hyperbeam
import razorleaf
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class BossPattern:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    STATES = ['Pattern1','Pattern2','Pattern3']
    images = {}
    FPS = {'Pattern1':1,'Pattern2':1,'Pattern3':1}
    LASER_INTERVAL = 0

    #constructor
    def __init__(self,state):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 500, 300
        self.delta = (0, -5)
        self.speed = 200
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
        self.state = state
        self.wh = ()
        self.width = 10
        self.height = 10
        self.flip = ''
        BossPattern.load_images()
        hyperbeam.HyperBeam.makeGetBBS()

    @staticmethod
    def load_images():
        images = {}
        file_fmt= '%s/미싱노패턴/%s/Animation-%d Direction-%d Frame-%d.png'

        for state in BossPattern.STATES:
            state_images = []
            n = -1
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR,state,0,0,n)
                if os.path.isfile(fn):
                    state_images.append(gfw.image.load(fn))
                else:
                    break
            n = -1
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR,state,4,0,n)
                if os.path.isfile(fn):
                    state_images.append(gfw.image.load(fn))
                else:
                    break
            n = - 1
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR,state,5,0,n)
                if os.path.isfile(fn):
                    state_images.append(gfw.image.load(fn))
                else:
                    break
            images[state] = state_images 
            
        BossPattern.images = images


    def do_Pattern(self):
        if self.state == 'Pattern1':
            rock = rockthrow.RockThrow(BossPattern.images[self.state],'Large',random.randint(60,280), 470,0,-5)
            gfw.world.add(gfw.layer.rock,rock)
        if self.state == 'Pattern2':
            beam = hyperbeam.HyperBeam(BossPattern.images[self.state],'Charge')
            gfw.world.add(gfw.layer.beam,beam)
        if self.state == 'Pattern3':
            leaf = razorleaf.RazorLeaf(BossPattern.images[self.state],'Ready')
            gfw.world.add(gfw.layer.leaf,leaf)


    def update(self):
        pass
    

