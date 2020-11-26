
import random
from pico2d import *
import gfw
import gobj
import math
import bossPattern
import boss_life_gauge
import boss_die_effect
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Boss:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    STATES = ['Idle','Dead','Pattern1','Pattern2','Pattern3','Chance','Die']
    images = {}
    FPS = 20
    LASER_INTERVAL = 0
    BossScale = 3.5
    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 0, 300
        self.delta = (0, -5)
        self.for_get_bb_pos = self.pos
        self.speed = 200
        self.rad = 0
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
        self.images = Boss.load_images()
        self.state = 'Idle'
        self.wh = ()
        self.shiledalpha = 100
        self.width = 10
        self.height = 10
        self.flip = ''
        self.die_time = 0
        self.explosion_time = 0
        self.dead = 0
        self.dead_explosion_cycle = 1.0
        self.ret_time = 0
        self.Pattern_time = 0
        self.chance_time = 0
        self.bulletnum = 0
        self.gravity = 0.1
        self.dtheta = 0
        self.HP = 100
        self.shield = True
        self.old_Pattern = ''
        self.Pattern_INFO = 0
        self.Pattern2Start = 0 # 빔 테스트 임시변수임
        self.build_behavior_tree()
        boss_life_gauge.load()
        self.music = load_wav('./res/미싱노브금/boss/explosionlong.wav')
        self.music.set_volume(gfw.Volume-10)
        self.winmusic = load_music('./res/미싱노브금/victory.ogg')
        self.winmusic.set_volume(gfw.Volume)
    @staticmethod
    def load_images():
        images = {}
        file_fmt_boss = '%s/보스/3827.png'
        file_fmt_shield = '%s/보스/6714.png'
        file_fmt_die = './res/보스/보스사망/Animation-4 Direction-0 Frame-%d.png'
        state_images = []
        state_shield = []
        state_die = []
        fn = file_fmt_boss % (gobj.RES_DIR)
        if os.path.isfile(fn):
            state_images.append(gfw.image.load(fn))
        images[0] = state_images
        fn = file_fmt_shield % (gobj.RES_DIR)
        if os.path.isfile(fn):
            state_shield.append(gfw.image.load(fn))
        images[1] = state_shield
        n = -1
        while True:
                n += 1
                fn = file_fmt_die % (n)
                if os.path.isfile(fn):
                    state_die.append(gfw.image.load(fn))
                else:
                    break
        images[2] = state_die

        return images

    def get_shield(self):
        return self.shield
    def set_shield_alpha(self):
        self.shiledalpha = 230
    def get_boss_die(self):
        return self.dead
    def get_bb(self):
        images = self.images[0]
        image = images[self.fidx % len(images)]
        x,y = self.for_get_bb_pos
        #24는 보스의 꺾이는 부분의 길이이다. h의반틈에서 24를 빼주면 꺾이는 부분
        return x - image.w*Boss.BossScale//2, y - image.h*Boss.BossScale//2, x + image.w*Boss.BossScale//2, y + (image.h//2-24)*Boss.BossScale
 
    def get_bb2(self):
       images = self.images[0]
       image = images[self.fidx % len(images)]
       x,y = self.for_get_bb_pos
       #마찬가지로 죄하단 x는 원본이미지 길이에서 7을 빼주면 되고, 좌하단 y는 get_bb에서 끝난 부분 부터 시작 하면 되므로 이렇게 해줌
       return x - (image.w//2-7)*Boss.BossScale, y + (image.h//2-24)*Boss.BossScale, x + image.w*Boss.BossScale//2, y + image.h*Boss.BossScale//2
 
    def hit(self):
        if self.HP > 0:
            self.HP -= 1
        if self.HP <= 0:
            if self.state != 'Dead':
                self.winmusic.play()
                self.winmusic.stop()
                for text in gfw.world.objects_at(gfw.layer.text):
                    text.set_text(text.TEXT_DIC['Victory'])    #text는 textbg를 objects_at 해오는거고, 이 객체에는 TEXT_DIC이라는
            self.state = 'Dead'

    def draw(self,posi):
        rate = self.HP / 100
        boss_life_gauge.draw(162, 367, 95, rate,posi)        
        for n in range(2):
            images = self.images[n]
            image = images[self.fidx % len(images)]
            result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
            self.for_get_bb_pos = result_posi
            if n == 0:
                image.composite_draw(self.rad,self.flip,*result_posi,image.w*Boss.BossScale,image.h*Boss.BossScale)
            elif n == 1:
                if self.shield == True:
                    if self.shiledalpha > 55:
                        self.shiledalpha-=1
                        
                    SDL_SetTextureAlphaMod(image.texture,self.shiledalpha)
                    image.composite_draw(0,self.flip,*result_posi,image.w*4,image.h*4)


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
            #     for text in gfw.world.objects_at(gfw.layer.text):
            #         text.set_text(text.TEXT_DIC[self.state])    #text는 textbg를 objects_at 해오는거고, 이 객체에는 TEXT_DIC이라는
            #         #클래스 변수가 있는데 여기에 적절한 값을 넣으면 알아서 튀어나옴
            #     if self.state != self.old_Pattern:
            #         break

            self.state = 'Pattern' + str(random.randint(2,2))
            #설정된 보스패턴으로 초기화
            self.Pattern_INFO = bossPattern.BossPattern(self.state)
            self.old_Pattern = self.state
            return BehaviorTree.FAIL


        self.pos = x,y
        # self.delta = dx,dy
        return BehaviorTree.SUCCESS

    def remove(self):
        gfw.world.remove(self)

    def do_die(self):
        if self.state != 'Dead':
           return BehaviorTree.FAIL
        old_pt_time = self.explosion_time // self.dead_explosion_cycle
        self.die_time += gfw.delta_time
        self.explosion_time += gfw.delta_time

        if self.dead != 1:
            if old_pt_time != self.explosion_time // self.dead_explosion_cycle:
                x,y = self.pos
                x += random.randint(-50,50)
                y += random.randint(-50,50)
                b_d_e = boss_die_effect.BossDieEffect((x,y),self.images[2])
                gfw.world.add(gfw.layer.boss_die_effect,b_d_e)
                if self.dead_explosion_cycle - 0.1 > 0.1:
                    self.dead_explosion_cycle -= 0.1
                if random.randrange(2) == 0:
                    self.rad = 15 * 3.14 / 180
                else :
                    self.rad = -15 * 3.14 / 180
                self.explosion_time = 0


            #x,y = self.pos
            #y -= 0.5
            #self.pos = x,y
        if self.die_time > 6.0:
            if self.dead == 0:
                self.music.play()
                self.winmusic.play()
            self.rad = 30
            self.dead = 1
            x,y = self.pos
            y -= 2
            self.pos = x,y


        return BehaviorTree.SUCCESS


    def do_chance(self):
        if self.state != 'Chance':
            return BehaviorTree.FAIL
        x,y = self.pos
        dx,dy = self.delta

        self.chance_time += gfw.delta_time
        if y >105:
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
        #pos = (self.pos[0], self.pos[1])
        x,y = self.pos
        self.time += gfw.delta_time

        self.ret_time += gfw.delta_time
        self.fidx = round(self.ret_time*Boss.FPS)

        if self.state != 'Dead':
            if self.time > 0.05:
                y = y + math.sin(self.dtheta*180/math.pi)*10
                #pos = (self.pos[0], self.pos[1] +
                #    math.sin(self.dtheta*180/math.pi)*10)
                self.dtheta = (self.dtheta+1) % 360
                self.time = 0
        if x + 5 <= 500:
            x += 5

        self.pos = x,y


        self.bt.run()

  
        
    def screenshake(self,pos):
        # if self.state == 'Dead':
        #     pos1 =(math.sin(self.dtheta*180/math.pi) * 5, math.sin(self.dtheta*180/math.pi) * 5)
        #     pos[0] = pos1
        #     self.dtheta = (self.dtheta+1) % 360   
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
                },
                {
                    "name":"Dead",
                    "class":LeafNode,
                    "function" : self.do_die
                }

            ]


        }
        )

