from pico2d import *
import gfw

canvas_width = 640
canvas_height = 480

def load():
    global fg,cong
    fg = gfw.image.load('./res/bg/2012.png')
    cong = gfw.image.load('./res/bg/cong.png')
    global mfont,notice
    mfont = gfw.font.load('./res/ConsolaMalgun.ttf',15)
    notice = gfw.font.load('./res/ConsolaMalgun.ttf',30)

def draw(name):
    global fg,cong,mfont
    fg.draw(canvas_width//2,canvas_height//2)
    mfont.draw(canvas_width//2-50,canvas_height//2,name,(0,0,0))
    cong.draw(canvas_width//2,canvas_height-100)
    mfont.draw(100,240,"type your name ->",(240,240,240))
    notice.draw(20,canvas_height//2 - 100 ,"Press 'Enter' to Record your records",(240,240,240))
