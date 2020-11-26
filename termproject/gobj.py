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

# def collides_boxes(a,b):
# 	if (hasattr(a,'get_bb') == False):
# 		reutrn False
	
# 	if (hasattr(b,'get_bbes')==False):
# 		return False


def collides_box(a, b):
	check = True

	if (hasattr(a,'get_bb')==False):
		return False
	
	if (hasattr(b,'get_bb')==False):
		return False

	arr = []
	if hasattr(b, 'get_bbs'):
		arr = b.get_bbs()


	(la, ba, ra, ta) = a.get_bb()
	(lb, bb, rb, tb) = b.get_bb()

	if hasattr(b,'get_bb2'):
		(lb2,bb2,rb2,tb2) = b.get_bb2()	
		if la > rb2: check = False
		if ra < lb2: check = False
		if ba > tb2: check = False
		if ta < bb2: check = False		#get_Bb2에서 없어도 걍 넘어감.
		if check == True:
			print("get_bb2와의 충돌")
			return True


	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False



	print("일반적인 충돌")

	return True

def draw_collision_box():
	for obj in gfw.world.all_objects():
		if hasattr(obj, 'get_bb'):
			draw_rectangle(*obj.get_bb())
		if hasattr(obj, 'get_bb2'):
			draw_rectangle(*obj.get_bb2())
		if hasattr(obj,'get_bbs'):
			for i in range(len(obj.get_bbs())):
				draw_rectangle(*obj.get_bbs()[i])

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")
