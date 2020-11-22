import gfw
from pico2d import *
import gobj
import main_state
import random


canvas_width = 640
canvas_height = 480

def enter():
    gfw.world.init([])

    global bg,name,light,start,rank,mquit,select
    bg = gfw.image.load('./res/bg/88.png')
    name = gfw.image.load('./res/bg/97.png')
    light = gfw.image.load('./res/bg/89.png')
    start = gfw.image.load('./res/bg/Start.png')
    rank = gfw.image.load('./res/bg/Rank.png')
    mquit = gfw.image.load('./res/bg/Quit.png')
    select = gfw.image.load('./res/bg/117.png')
    global lightning,light_time
    lightning = 0
    light_time = 0
    
    global selecty,selected
    selecty = 240
    selected = 3
    
def lightfunc():
    global light_time,lightning
    light_time += gfw.delta_time
    if light_time > random.uniform(3.0,4.0):
        lightning = 160
        light_time = 0

    if lightning- 3 >= 0:
        lightning -= 3
    SDL_SetTextureAlphaMod(light.texture,lightning)
        

def update():
    gfw.world.update()
    lightfunc()
    check()

def check():
    pass

    

def draw():
    bg.draw(320,240)
    light.draw(320,240)
    name.draw(320,340)
    start.draw(320,190)
    rank.draw(320,120)
    mquit.draw(320,50)
    select.draw(320,selecty)
    
    gfw.world.draw()

def pause():
    pass

def handle_event(e):
    global selecty,selected
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_DOWN:
            if selecty - 70 >30 :
                selecty -= 70
                selected -= 1
        elif e.key == SDLK_UP:
            if selecty + 70 <=240:
                selecty += 70
                selected += 1
        elif e.key == SDLK_RETURN:
            if selected == 3:
                gfw.push(main_state)

def resume():
    enter()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()


