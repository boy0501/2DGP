import gfw
from pico2d import *
import start_state


def enter():
    global image, elapsed ,bg
    image = load_image('./res/kpu_credit.png')
    bg = load_image('./res/bg/89.png')
    elapsed = 0

def update():
    global elapsed
    elapsed += gfw.delta_time
    if elapsed > 4.0:
        gfw.change(start_state)

def draw():
    bg.draw(320,240)
    normalize = elapsed / 4
    if normalize <= 0.5:
        alpha = elapsed * 255 / 2
    else :
        alpha = 255 - elapsed * 255 / 2

    SDL_SetTextureAlphaMod(image.texture,int(alpha))
    image.draw(320, 240)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
