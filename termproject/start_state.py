import gfw
from pico2d import *
import gobj


canvas_width = 640
canvas_height = 480

def enter():
    gfw.world.init(['bg', 'bullet','player','boss','rock','beam','leaf','blood','text','die'])
    

def update():
    gfw.world.update()
    check()

def check():
    pass

    

def draw():
    gfw.world.draw()


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()


