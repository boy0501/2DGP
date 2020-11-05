import random
from pico2d import *
import gfw
import math

RES_DIR = './res'
canv_width = 640
canv_height =480
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
	if hasattr(b,'get_bb2'):
		(lb2,bb2,rb2,tb2) = b.get_bb2()	
		if la > rb2: return False
		if ra < lb2: return False
		if ba > tb2: return False
		if ta < bb2: return False
		print("용캐도 여기까지 왔군")

	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False




	return True

def draw_collision_box():
	for obj in gfw.world.all_objects():
		if hasattr(obj, 'get_bb'):
			draw_rectangle(*obj.get_bb())
		if hasattr(obj, 'get_bb2'):
			draw_rectangle(*obj.get_bb2())

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")
