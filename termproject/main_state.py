import gfw
from pico2d import *
from player import Player
from bullet import Bullet
import gobj


canvas_width = 640
canvas_height = 480

def enter():
    gfw.world.init(['bg', 'bullet','player'])
    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    bg = gobj.ImageObject('1770.png', canvas_width //2, canvas_height //2)
    gfw.world.add(gfw.layer.bg, bg)

def update():
    gfw.world.update()


def draw():
    gfw.world.draw()


def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()


