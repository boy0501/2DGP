
import random
from pico2d import *
import gfw
import gobj
import math
import bossPattern
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Boss:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    STATES = ['Idle','Dead','Pattern1','Pattern2','Pattern3','Chance']
    images = {}
    FPS = 1
    LASER_INTERVAL = 0

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 500, 300
        self.delta = (0, -5)
        self.speed = 200
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
        self.images = Boss.load_images()
        self.state = 'Idle'
        self.wh = ()
        self.width = 10
        self.height = 10
        self.flip = ''
        self.ret_time = 0
        self.Pattern_time = 0
        self.chance_time = 0
        self.bulletnum = 0
        self.gravity = 0.1
        self.dtheta = 0
        self.shield = True
        self.old_Pattern = ''
        self.Pattern_INFO = 0
        self.Pattern2Start = 0 # 빔 테스트 임시변수임
        self.build_behavior_tree()

    @staticmethod
    def load_images():
        images = {}
        file_fmt_boss = '%s/보스/3827.png'
        file_fmt_shield = '%s/보스/6714.png'
        state_images = []
        state_shield = []
        fn = file_fmt_boss % (gobj.RES_DIR)
        if os.path.isfile(fn):
            state_images.append(gfw.image.load(fn))
        images[0] = state_images
        fn = file_fmt_shield % (gobj.RES_DIR)
        if os.path.isfile(fn):
            state_shield.append(gfw.image.load(fn))
        images[1] = state_shield
        return images



 

    def draw(self,posi):
        
        for n in range(2):
            images = self.images[n]
            image = images[self.fidx % len(images)]
            result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
            if n == 0:
                image.composite_draw(0,self.flip,*result_posi,85,200)
            elif n == 1:
                if self.shield == True:
                    image.composite_draw(0,self.flip,*result_posi,180,250)


       # image.composite_draw(0,self.flip,*result_posi,self.width,self.height)
    def do_idle(self):
        
        if self.state != 'Idle':
            return BehaviorTree.FAIL

        x,y = self.pos
        if y <300:
            y +=  500 * gfw.delta_time

        if self.ret_time > 2:
            # while True:
            #     self.state = 'Pattern' + str(random.randint(1,3))
            #     if self.state != self.old_Pattern:
            #         break

            self.state = 'Pattern' + str(random.randint(3,3))
            #설정된 보스패턴으로 초기화
            self.Pattern_INFO = bossPattern.BossPattern(self.state)
            self.old_Pattern = self.state
            return BehaviorTree.FAIL


        self.pos = x,y
        # self.delta = dx,dy
        return BehaviorTree.SUCCESS

    def do_chance(self):
        if self.state != 'Chance':
            return BehaviorTree.FAIL
        x,y = self.pos
        dx,dy = self.delta

        self.chance_time += gfw.delta_time
        if y >75:
            y -=  800 * gfw.delta_time



        self.delta = dx,dy
        self.pos = x,y
        if self.chance_time > 2:
            self.state = 'Idle'
            self.ret_time = 0 
            self.chance_time = 0
            self.shield = True
            return BehaviorTree.FAIL

        return BehaviorTree.SUCCESS



    def do_pattern1(self):
        if self.state!='Pattern1':
            return BehaviorTree.FAIL
        #정수연산을 해주기 위해서 pattern_time 을 //1 해서 old_pt_time에 정수로 저장해준다. 시간초가 바뀌면 돌 하나씩 생성해줄것임.
        old_pt_time = self.Pattern_time // 1

        self.Pattern_time += gfw.delta_time
        if self.Pattern_time > 11:
            self.Pattern_time = 0
            self.state = 'Chance'
            self.shield = False
            return BehaviorTree.FAIL

        if old_pt_time != self.Pattern_time // 1:
            bossPattern.BossPattern.do_Pattern(self.Pattern_INFO)
            #self.Pattern_time = 0

        return BehaviorTree.SUCCESS

    def do_pattern2(self):
        if self.state!='Pattern2':
            return BehaviorTree.FAIL
        self.Pattern_time += gfw.delta_time
        if self.Pattern_time > 6.5:
            self.Pattern_time = 0
            self.Pattern2Start = 0
            self.state = 'Chance'
            self.shield = False
            return BehaviorTree.FAIL
        if self.Pattern2Start == 0:
            bossPattern.BossPattern.do_Pattern(self.Pattern_INFO)
        self.Pattern2Start = 1

        return BehaviorTree.SUCCESS

    def do_pattern3(self):
        if self.state!='Pattern3':
            return BehaviorTree.FAIL
        old_pt_time = self.Pattern_time // 0.1

        self.Pattern_time += gfw.delta_time
        if self.Pattern_time > 5.0:
            self.Pattern_time = 0
            self.state = 'Chance'
            self.shield = False
            return BehaviorTree.FAIL

        if self.Pattern_time < 2.5 :
            if old_pt_time != self.Pattern_time // 0.1:
                bossPattern.BossPattern.do_Pattern(self.Pattern_INFO)
        
        return BehaviorTree.SUCCESS

    def update(self):
        
        #보스는 어떠한 상황이던간에 위아래로 움직인다. 그래서 공통으로 넣음
        #함수로 묶을 수 있으나,,, 나중에 해야징징이
        pos = (self.pos[0], self.pos[1])
        
        self.time += gfw.delta_time

        self.ret_time += gfw.delta_time


        if self.time > 0.05:
            pos = (self.pos[0], self.pos[1] +
                math.sin(self.dtheta*180/math.pi)*10)
            self.dtheta = (self.dtheta+1) % 360
            self.time = 0

        self.pos = pos
        self.fidx = round(self.time*Boss.FPS)


        self.bt.run()

  
        
    def screenshake(self,pos):
        pass       
        

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)        

    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name":"BossState",
            "class":SelectorNode,
            "children":[
                {
                    "name":"Chance",
                    "class":LeafNode,
                    "function" : self.do_chance
                },
                {
                    "name":"Idle",
                    "class":LeafNode,
                    "function" : self.do_idle
                },
                {
                    "name":"Pattern",
                    "class":SelectorNode,
                    "children":[
                        {
                            "name":"Pattern1",
                            "class":LeafNode,
                            "function" : self.do_pattern1
                        },
                        {
                            "name":"Pattern2",
                            "class":LeafNode,
                            "function" : self.do_pattern2
                        },
                        {
                            "name":"Pattern3",
                            "class":LeafNode,
                            "function" : self.do_pattern3
                        },
                    ]
                }

            ]


        }
        )

