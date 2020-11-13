
import random
from pico2d import *
import gfw
import gobj


canvas_width = 640
canvas_height = 480

class Background:
    FPS = 12
    image_ground = []
    BACK_INFO = [ 
        {
            "name":"Platform",
            "code":3818,
            "x":320,
            "y":240
        },
        {
            "name":"Name",
            "code":3750,
            "x":150,
            "y":400
        },
        {
            "name":"BossHP",
            "code":3859,
            "x":150,
            "y":370
        },
        {
            "name":"Ground",
            "code":3818,
            "x":320,
            "y":240
        },
        {
            "name":"YouDie",
            "code":468,
            "x":320,
            "y":240
        },
        {
            "name":"Words",
            "code":3842,
            "x":20,
            "y":10
            #가로 14
            #세로 18 이 한칸 
        }
    ]
    BACK_INFO_NAME = ["name","BossHP","Ground","YouDie"]
    TEXT_DIC ={
        "Pattern1" : 'Enemy MISSINGNO. used ROCK THROW!',
        "Pattern2" : "Enemy MISSINGNO. is charging its lazor!",
        "Beam" : "Enemy MISSINGNO. used HYPER BEAM!",
        "Pattern3" : "Enemy MISSINGNO. used RAZOR LEAF!",
        "Die" : "BOSHY fainted!",
        "Appear" : "wild MISSINGNO. appeared!"
    }
    TEXT_INFO ={
        # 18, 36, 54 ,72,90,108+126 가 아래서부터 세로 순서
        # 14, 28, 42, 56,70,84,98,112,126,140,154,168,182,196,210,224,238,252,266,280,294,308,322,336,350,364,378,392,406,420,434,448
        #총 32행 7열 있음
        # 대문자 A는 2행 6열 
        # 소문자 A는 2행 5열 에서 시작 
        " ":(0,108),
        "!":(14,108),
        ".":(196,108),
        "A":(14,90),
        "B":(28,90),
        "C":(42,90),
        "D":(56,90),
        "E":(70,90),
        "F":(84,90),
        "G":(98,90),
        "H":(112,90),
        "I":(126,90),
        "J":(140,90),
        "K":(154,90),
        "L":(168,90),
        "M":(182,90),
        "N":(196,90),
        "O":(210,90),
        "P":(224,90),
        "Q":(238,90),
        "R":(252,90),
        "S":(266,90),
        "T":(280,90),
        "U":(294,90),
        "V":(308,90),
        "W":(322,90),
        "X":(336,90),
        "Y":(350,90),
        "Z":(364,90),

        "a":(14,72),
        "b":(28,72),
        "c":(42,72),
        "d":(56,72),
        "e":(70,72),
        "f":(84,72),
        "g":(98,72),
        "h":(112,72),
        "i":(126,72),
        "j":(140,72),
        "k":(154,72),
        "l":(168,72),
        "m":(182,72),
        "n":(196,72),
        "o":(210,72),
        "p":(224,72),
        "q":(238,72),
        "r":(252,72),
        "s":(266,72),
        "t":(280,72),
        "u":(294,72),
        "v":(308,72),
        "w":(322,72),
        "x":(336,72),
        "y":(350,72),
        "z":(364,72),

    }
    TYPE_TIME = 0.1     #글자 띄워지는 주기


    @staticmethod
    def load_back_images():
        images = []
        file_fmt = '%s/보스/보스방/Animation-%d Direction-%d Frame-%d 복사.png'
        action_images = []
        n = -1
        while True:
            n += 1

            fn = file_fmt % (gobj.RES_DIR,0,0,n)
            if os.path.isfile(fn):
                action_images.append(gfw.image.load(fn))
            else:
                break
        images = action_images
        return images

    @staticmethod
    def load_back_image():#이거는 이제 배경 이미지들이 아닌 각각의 개체를 저장하려고 하는것
        file_fmt = '%s/보스/%d.png'
        for name in Background.BACK_INFO:
            fn = file_fmt %(gobj.RES_DIR,name['code'])
            if os.path.isfile(fn):
                Background.image_ground.append(gfw.image.load(fn))

            




    def __init__(self,select = 0,Text = "wild MISSINGNO. appeared!"):
        Background.load_back_image()
        self.image = Background.load_back_images()
        self.x, self.y = canvas_width//2, canvas_height//2
        self.dx,self.dy=0.0,0.0
        self.dtheta = 0
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
        self.death_img = 0
        self.selectbg = select  #0이면 일반배경 1이면 die배경 
        self.text = Text
        self.textlen = 0    #현재 몇개의 텍스트가 출력되어야 하는지.
        

    def set_death_img_to_die(self):
        self.death_img = 1

    def set_text(self,Text):
        self.text = Text
        self.textlen = 0

    def draw(self,pos):
        images = self.image
        image = images[self.fidx % len(images)]
        #배경그리는곳
        
        if self.selectbg == 0:
            image.clip_draw(0,0,700,500,320+pos[0],240+pos[1])
            for n in range(4):
                Background.image_ground[n].draw(Background.BACK_INFO[n]["x"]+pos[0],Background.BACK_INFO[n]["y"]+pos[1])
        elif self.selectbg == 1:
            if self.death_img == 1:
                Background.image_ground[4].draw(Background.BACK_INFO[4]["x"]+pos[0],Background.BACK_INFO[4]["y"]+pos[1])
        elif self.selectbg == 2:
            i = 20
            for words in range(self.textlen):
                wordpos = Background.TEXT_INFO[self.text[words]]
                Background.image_ground[5].clip_draw(*wordpos,14,18,i+pos[0],20+pos[1])
                i+=14
            # for words in self.text:
            #     wordpos = Background.TEXT_INFO[words]
            #     Background.image_ground[5].clip_draw(*wordpos,14,18,i,250)
            #     i+=14

        #self.image.draw(self.x+pos[0], self.y+pos[1])
    def update(self):
        self.dy = math.sin(self.dtheta*180/math.pi) * 10
        self.dx = math.sin(self.dtheta*180/math.pi) * 10
        self.dtheta = (self.dtheta+1)%360
        self.time += gfw.delta_time
        self.fidx = round(self.time*Background.FPS) 
        if self.selectbg ==2:
            if self.textlen < len(self.text):
                self.time += gfw.delta_time
                if self.time > Background.TYPE_TIME:
                    self.textlen += 1
                    self.time = 0

    def screenshake(self,pos):
        pass       
        
   

