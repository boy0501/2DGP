
import random
from pico2d import *
import gfw
import gobj


canvas_width = 640
canvas_height = 480

class Background:
	FPS = 12
	image_ground = []

	@staticmethod
	def load_images():
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


	def __init__(self):
		#self.image = self.imagegfw.image.load('./res/bg/1770.png')
		Background.image_ground.append(gfw.image.load('./res/보스/3818.png'))
		self.image = Background.load_images()
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
		Background.image_ground[0].clip_draw(0,0,700,500,320+pos[0],240+pos[1])
		#self.image.draw(self.x+pos[0], self.y+pos[1])
	def update(self):
		self.dy = math.sin(self.dtheta*180/math.pi) * 10
		self.dx = math.sin(self.dtheta*180/math.pi) * 10
		self.dtheta = (self.dtheta+1)%360
		self.time += gfw.delta_time
		self.fidx = round(self.time*Background.FPS)		
		
   

