import random
from pico2d import *
import gfw
import math

RES_DIR = './res'

def rand(val):
	return val * random.uniform(0.9, 1.1)

def point_add(point1, point2):
	x1,y1 = point1
	x2,y2 = point2
	return x1+x2, y1+y2

def move_obj(obj):
	obj.pos = point_add(obj.pos, obj.delta)

def collides_box(a, b):
	(la, ba, ra, ta) = a.get_bb()
	(lb, bb, rb, tb) = b.get_bb()

	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False

	return True

def draw_collision_box():
	for obj in gfw.world.all_objects():
		if hasattr(obj, 'get_bb'):
			draw_rectangle(*obj.get_bb())

   

class ImageObject:

	FPS = 12
	image_ground = []

	@staticmethod
	def load_images():
		images = []
		file_fmt = '%s/미싱노패턴/보스방/Animation-%d Direction-%d Frame-%d 복사.png'
		action_images = []
		n = -1
		while True:
			n += 1

			fn = file_fmt % (RES_DIR,0,0,n)
			if os.path.isfile(fn):
				action_images.append(gfw.image.load(fn))
			else:
				break
		images = action_images
		return images


	def __init__(self, imageName, x, y):
		#self.image = self.imagegfw.image.load('./res/bg/1770.png')
		ImageObject.image_ground = gfw.image.load('./res/미싱노패턴/보스방/3818.png')
		self.image = ImageObject.load_images()
		self.x, self.y = x, y
		self.dx,self.dy=0.0,0.0
		self.dtheta = 0
		self.fidx = 0 #fps 의 dx이다
		self.time = 0
	def draw(self,pos):
		images = self.image
		image = images[self.fidx % len(images)]
		#배경그리는곳
		
		image.clip_draw(0,0,700,500,320+pos[0],240+pos[1])
		ImageObject.image_ground.clip_draw(0,0,700,500,320+pos[0],240+pos[1])
		#self.image.draw(self.x+pos[0], self.y+pos[1])
	def update(self):
		self.dy = math.sin(self.dtheta*180/math.pi) * 10
		self.dx = math.sin(self.dtheta*180/math.pi) * 10
		self.dtheta = (self.dtheta+1)%360
		self.time += gfw.delta_time
		self.fidx = round(self.time*ImageObject.FPS)		
		

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")
