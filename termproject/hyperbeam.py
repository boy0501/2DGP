
import random
from pico2d import *
import gfw
import gobj
import math
import player

class HyperBeam:
    SPECIAL_KEY_MAP ={
    (SDL_KEYDOWN, SDLK_LSHIFT): 7,
    (SDL_KEYDOWN, SDLK_z): 14,
    (SDL_KEYUP,SDLK_LSHIFT): 8  
    }
    #뒤에있는 숫자는 이미지파일의 시작 인덱스이다.
    STATES = {'Beam':0,'Charge':5,'Energy':11}
    #돌에대한 이미지만 받을것이기떄문에 dic이 아닌 list
    images = []
    FPS = {'Beam':5,'Charge':6,'Energy':3}
    beampix = 16 * 7 #원본이미지에 8배 곱해준것
    IMAGESIZE_GETBB ={'Beam':[(16,16),(16,16),(16,16),(16,16),(16,16)],
                'Charge':[(20,22),(20,20),(20,20),(20,20),(20,20),(20,20)],
                'Energy':[(5,5),(5,5),(5,5)]
    }

    IMAGESIZE_GETBBS = {
        # 대각선 길이는 가로 2 세로 8의 형태를 가진다.
        'Frame0':[(0,0,16,16)],
        'Frame1':[(0,0,16,16)],
        'Frame2':[(0,0,16,16)],
        'Frame3':[(0,0,16,16)],
        'Frame4':[(0,0,16,16)]
    }
    #각 그림당 필요한 대각선의 갯수
    IMAGESIZE_DIAG = [0,8,16,24,24]
    #500,350은 보스의 위치임 ㅇㅇ,,,,,,, 이게 뭔가 했네 자꾸 그럼 보스위치에서부터 이미지가 나와야할 중점을 말하는거
    BEAM = [(500-beampix/2,350-beampix/2),(500-beampix,350-beampix*3/4),(500-beampix*3/2,350-beampix),
    (500-beampix*39/16,350-beampix*25/16),(500-beampix*39/16,350-beampix*25/16)]
    LASER_INTERVAL = 0

    @staticmethod
    def makeGetBBS():
        for i in range(HyperBeam.FPS['Beam']):
            for j in range(HyperBeam.IMAGESIZE_DIAG[i]):
                if i == 3:
                    HyperBeam.IMAGESIZE_GETBBS['Frame' + str(i)].append((31+j*2 , 20+ j , 31 + (j+1)*2 , 20+ j + 8))
                else:
                    HyperBeam.IMAGESIZE_GETBBS['Frame' + str(i)].append((16+j*2 , 9 + j , 16 + (j+1)*2 , 9 + j + 8))




    #constructor
    def __init__(self,image,state,x=500,y=300):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = x,y
        self.delta = 1,0
        self.for_get_bb_pos = self.pos
        self.speed = 2
        self.gravity = 10
        self.time = 0
        self.width = 10
        self.height = 10
        self.dtheta = 0
        self.shaketime = 0
        self.Chargingtime = 3.5
        self.Firetime = 3.0
        self.EnergyRe_gentime = 0.05
        self.Energytime = 0
        self.delaytime = 1.2
        self.Scale = 1.0
        self.fidx = 0
        self.beamtarget = 0,0
        self.state = state
        self.rad = 0
        self.radb = 0
        self.shakeWH = 40
        HyperBeam.images = image
        self.music = load_wav('./res/미싱노브금/boss/hyperbeam.wav')
        self.music.set_volume(gfw.Volume)
        self.music_on = False





    def draw(self,posi):
        # if self.laser_time < Player.LASER_INTERVAL:
        #     self.state = 'Attack'
        # images = self.images[self.state]
        # image = images[self.fidx % len(images)]
        # result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
        # self.width = Player.IMAGESIZE[self.state][self.fidx%len(images)][0]       
        # self.height = Player.IMAGESIZE[self.state][self.fidx%len(images)][1]
        # image.composite_draw(0,self.flip,*result_posi)   
        if self.time > self.delaytime or self.state!='Beam': 
            if(self.state == 'Beam'):
                self.pos = HyperBeam.BEAM[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]
            result_posi = (self.pos[0] + posi[0],self.pos[1]+posi[1])
            self.for_get_bb_pos = result_posi
            image = HyperBeam.images[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]
            self.width = HyperBeam.IMAGESIZE_GETBB[self.state][self.fidx % HyperBeam.FPS[self.state]][0]       
            self.height = HyperBeam.IMAGESIZE_GETBB[self.state][self.fidx % HyperBeam.FPS[self.state]][1]
            image.composite_draw(self.rad,'',*result_posi,image.w*self.Scale,image.h*self.Scale)
       #image.draw(*self.pos,100,100)

    def get_bb(self):
        image =  HyperBeam.images[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]
        x,y = self.for_get_bb_pos
        if self.state != 'Beam':
            return x - self.width* self.Scale//2, y - self.height* self.Scale//2, \
            x + self.width* self.Scale//2, y + self.height* self.Scale//2      
        else :
            if self.time > self.delaytime:
                # x - image.w * self.Scale//2 이게 이미지의 좌하단 이미지임
                #arr = []
                #arr.append(x - image.w* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][0] * self.Scale, y - image.h* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][1] * self.Scale, \
                #x - image.w * self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][2] * self.Scale , y - image.h* self.Scale//2 + + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][3] * self.Scale)

                #return x - image.w* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][0] * self.Scale, y - image.h* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][1] * self.Scale, \
                #x - image.w * self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][2] * self.Scale , y - image.h* self.Scale//2 + + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][3] * self.Scale 

                return x - image.w* self.Scale//2, y - image.h* self.Scale//2, \
                x - image.w * self.Scale//2 + 32 * self.Scale//2 , y - image.h* self.Scale//2 + 32 * self.Scale//2   
            else :
                return 0,0,0,0

    def get_bbline(self):
        image =  HyperBeam.images[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]
        x,y = self.for_get_bb_pos
        return x - image.w* self.Scale//2, y - image.h* self.Scale//2, \
        x - image.w * self.Scale//2 + 32 * self.Scale//2 , y - image.h* self.Scale//2 + 32 * self.Scale//2   
        


    def get_bbs(self):
        image =  HyperBeam.images[HyperBeam.STATES[self.state] + self.fidx % HyperBeam.FPS[self.state]]
        x,y = self.for_get_bb_pos
        arr = []
        if self.state == 'Beam':
            if self.time > self.delaytime:
            # x - image.w * self.Scale//2 이게 이미지의 좌하단 이미지임
            
            #arr.append((x - image.w* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][0] * self.Scale, y - image.h* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][1] * self.Scale, \
            #x - image.w * self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][2] * self.Scale , y - image.h* self.Scale//2 + + HyperBeam.IMAGESIZE_GETBBS['Beam1'][0][3] * self.Scale))
                fnum = self.fidx % HyperBeam.FPS[self.state]
                for i in range(len(HyperBeam.IMAGESIZE_GETBBS['Frame'+str(fnum)])):
                    arr.append((x - image.w* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Frame'+str(fnum)][i][0] * self.Scale, y - image.h* self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Frame'+str(fnum)][i][1] * self.Scale, \
                    x - image.w * self.Scale//2 + HyperBeam.IMAGESIZE_GETBBS['Frame'+str(fnum)][i][2] * self.Scale , y - image.h* self.Scale//2 +  HyperBeam.IMAGESIZE_GETBBS['Frame'+str(fnum)][i][3] * self.Scale))
    

                return arr
        return arr


    def EnergyMove(self):
        targetx = 500
        targety = 300
        x,y = self.pos
        dx = (targetx - x)/15
        dy = (targety - y)/15
        x += dx
        y += dy
        self.pos = x,y 

    def setBeamtuple(self):
        originalx = math.cos(0)
        originaly = math.sin(0)
        dx = math.cos(self.rad)
        dx = originalx - dx
        dy = math.sin(self.rad)
        dy = originaly - dy
        #500,350 즉 보스의 위치에서 beampix 보스의 이미지크기 의 /2 를 해서 중점을 찾아줌(제일 작은 이미지 기준)
        # /2가 0 , 3/2 39/16 되는건 처음 이미지에 대한 각 이미지의 크기 비율임.
        if (self.rad*180/math.pi) > 0:
            HyperBeam.BEAM = [
        (dx*HyperBeam.beampix +     500-HyperBeam.beampix/2 ,        dy*HyperBeam.beampix +             350-HyperBeam.beampix/2),
        (dx*HyperBeam.beampix*2 +   500-HyperBeam.beampix,           dy*HyperBeam.beampix*3/2 +          350-HyperBeam.beampix*3/4),
        (dx*HyperBeam.beampix*3 +   500-HyperBeam.beampix*3/2,       dy*HyperBeam.beampix*2 +           350-HyperBeam.beampix),
        (dx*HyperBeam.beampix*39/8 + 500-HyperBeam.beampix*39/16,    dy*HyperBeam.beampix*25/8   +     350-HyperBeam.beampix*25/16),
        (dx*HyperBeam.beampix*39/8 + 500-HyperBeam.beampix*39/16,    dy*HyperBeam.beampix*25/8    +    350-HyperBeam.beampix*25/16)]
        elif (self.rad * 180 /math.pi) <= 0:
            HyperBeam.BEAM =[
        (-dx*HyperBeam.beampix +     500-HyperBeam.beampix/2 ,        dy*HyperBeam.beampix +             350-HyperBeam.beampix/2),
        (-dx*HyperBeam.beampix*2 +   500-HyperBeam.beampix,           dy*HyperBeam.beampix*3/2 +          350-HyperBeam.beampix*3/4),
        (-dx*HyperBeam.beampix*3 +   500-HyperBeam.beampix*3/2,       dy*HyperBeam.beampix*2 +           350-HyperBeam.beampix),
        (-dx*HyperBeam.beampix*39/8 + 500-HyperBeam.beampix*39/16,    dy*HyperBeam.beampix*25/8   +     350-HyperBeam.beampix*25/16),
        (-dx*HyperBeam.beampix*39/8 + 500-HyperBeam.beampix*39/16,    dy*HyperBeam.beampix*25/8    +    350-HyperBeam.beampix*25/16)]

    def BossAndPlayer_Calcul_rad(self):
        c = math.dist((500,300),(50,40))        #lineAB
        a = math.dist(self.beamtarget,(50,40))  #lineBC
        b = math.dist((500,300),self.beamtarget)#lineAC
        self.rad = math.acos((b**2+c**2 - a**2)/(2*b*c))
        #500,300 과 0,0 을 잇는 직선보다 플레이어가 위에 있다면 rad은 거꾸로 돌아간거니 -1곱함
        if 3*self.beamtarget[0]/5 - self.beamtarget[1] < 0:
            self.rad *= -1

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time*HyperBeam.FPS[self.state])
        
        if self.state == 'Charge':
            self.rad+=0.1
            self.Scale += 0.01 
            self.Energytime += gfw.delta_time
            if self.Energytime > self.EnergyRe_gentime:
                self.Energytime = 0
                randomtheta = random.randint(0,360)
                randx = math.cos(randomtheta*180/math.pi)*150 +500
                randy = math.sin(randomtheta*180/math.pi)*150 +300
                energy = HyperBeam(HyperBeam.images, 'Energy', randx,randy)
                gfw.world.add(gfw.layer.beam, energy)
        if self.time > self.Chargingtime:
            if self.state == 'Charge':
                for text in gfw.world.objects_at(gfw.layer.text):
                    text.set_text(text.TEXT_DIC['Beam'])
            self.time = 0
            self.state = 'Beam'
            self.pos = gobj.canv_width//2,gobj.canv_height//2
            self.beamtarget = player.Player.PlayerPos
            self.Scale = 7
            #HyperBeam.beampix *= 7
            self.BossAndPlayer_Calcul_rad()
            #self.rad = 0 
            #self.rad = 0
            self.setBeamtuple()
        if self.state =='Beam':
            if self.time > self.delaytime:
                if self.music_on == False:
                    self.music.play()
                    self.music_on = True
            if self.time > self.Firetime:
                self.remove()
        if self.state == 'Energy':
            self.EnergyMove()
            if self.pos[0]<510 and self.pos[0]>490:
                if self.pos[1]<310 and self.pos[1]>290:
                    self.remove()




        # if y <-10:
        #     self.remove()


    def screenshake(self,pos):
        if self.state == 'Beam':
            self.shaketime += gfw.delta_time
            if self.shaketime > self.delaytime:
                pos1 =(math.sin(self.dtheta*180/math.pi) * self.shakeWH, math.sin(self.dtheta*180/math.pi) * self.shakeWH)
                pos[0] = pos1
                self.dtheta = (self.dtheta+1) % 360
                self.shakeWH -= 0.2877

        # if self.shaketime > 1:
        #     self.shaketime = 0
        pass


    def remove(self):
        #print((Bullet.bullets))
        gfw.world.remove(self)
        #print(Bullet.bullets)
        
    



    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)        
