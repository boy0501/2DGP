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
	def __init__(self, imageName, x, y):
		self.image = gfw.image.load(RES_DIR + '/' + imageName)
		self.x, self.y = x, y
		self.dx,self.dy=0.0,0.0
		self.dtheta = 0
	def draw(self,pos):
		#배경그리는곳
		self.image.draw(self.x+pos[0], self.y+pos[1])
	def update(self):
		self.dy = math.sin(self.dtheta*180/math.pi) * 10
		self.dx = math.sin(self.dtheta*180/math.pi) * 10
		self.dtheta = (self.dtheta+1)%360
		

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")