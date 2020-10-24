
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
            "name":"Words",
            "code":3842,
            "x":20,
            "y":10
        }
    ]
    BACK_INFO_NAME = ["name","BossHP","Ground"]




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

            




    def __init__(self):
        Background.load_back_image()
        self.image = Background.load_back_images()
        self.x, self.y = canvas_width//2, canvas_height//2
        self.dx,self.dy=0.0,0.0
        self.dtheta = 0
        self.fidx = 0 #fps 의 dx이다
        self.time = 0
    def draw(self,pos):
        images = self.image
        image = images[self.fidx % len(images)]
        #배경그리는곳
        image.clip_draw(0,0,700,500,320+pos[0],240+pos[1])
        for n in range(4):
            Background.image_ground[n].draw(Background.BACK_INFO[n]["x"]+pos[0],Background.BACK_INFO[n]["y"]+pos[1])
        #self.image.draw(self.x+pos[0], self.y+pos[1])
    def update(self):
        self.dy = math.sin(self.dtheta*180/math.pi) * 10
        self.dx = math.sin(self.dtheta*180/math.pi) * 10
        self.dtheta = (self.dtheta+1)%360
        self.time += gfw.delta_time
        self.fidx = round(self.time*Background.FPS)        
        
   

