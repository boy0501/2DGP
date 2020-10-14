import random
from pico2d import *
import gfw
import gobj

class Bullet:
    PAT_POSITIONS = [
        (43, 210), (1118, 210), (1050, 430), (575, 740), 
        (235, 927), (575, 740), (1050, 430), (1118, 210)
    ]
    ACTIONS = ['Attack', 'Dead', 'Idle', 'Walk']
    images = {}
    FPS = 12
    # FCOUNT = 10

    def get_bb(self):
        x,y = self.pos
        return x - 40, y - 50, x + 40, y + 40

    def __init__(self,x,y,speed):
        # if len(Bullet.images) == 0:
        #     self.load_images('male')
        #     self.load_images('female')

        self.pos = (0,0
        )
        self.delta = 0.1, 0.1
        self.find_nearest_pos()
        char = random.choice(['male', 'female'])
        self.load_images(char)
        self.action = 'Walk'
        self.speed = 200
        self.fidx = 0
        self.time = 0

    def load_images(self, char):
        if char in Bullet.images:
            self.images = Bullet.images[char]
            return
        images = {}
        count = 0
        file_fmt = '%s/Bulletfiles/%s/%s (%d).png'
        for action in Bullet.ACTIONS:
            action_images = []
            count = 0
            while True:
                n = count + 1
                fn = file_fmt % (gobj.RES_DIR, char, action, n)
                try:
                    action_images.append(gfw.image.load(fn))
                except IOError:
                    break
                count = n
            images[action] = action_images
        self.images = images
        print('%d images loaded for %s' % (count, char))
        Bullet.images[char] = images

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Bullet.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        # print(self.pos, self.delta, self.target, x, y, dx, dy)

        done = False
        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or y < 0 and y <= ty:
            y = ty
            done = True

        self.pos = x,y

        if done:
            self.set_patrol_target()


    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.composite_draw(0, flip, *self.pos, 100, 100)