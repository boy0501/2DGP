from pico2d import *
import gfw
import gobj

def load():
    global fg
    fg = gfw.image.load('./res/보스/131.png')

def draw(x, y, width, rate,pos):
    global fg
    l = x - width // 2
    b = y - 5 // 2
    draw_3(fg, l, b, round(width * rate), 2,pos)

def draw_3(img, l, b, width, edge,pos):
    img.clip_draw_to_origin(0, 0, edge, img.h, l+pos[0], b+pos[1], edge, img.h)
    img.clip_draw_to_origin(edge, 0, img.w - 2 * edge, img.h, l+edge+pos[0], b+pos[1], width - 2 * edge, img.h)
    img.clip_draw_to_origin(img.w - edge, 0, edge, img.h, l+width-edge+pos[0], b+pos[1], edge, img.h)
