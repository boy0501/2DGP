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
    
    global Sbutton,Rbutton,Qbutton,Smag,Rmag,Qmag
    Smag = Rmag = Qmag = 1

    global mfont
    mfont = gfw.font.load('./res/ConsolaMalgun.ttf',15)
    
def lightfunc():
    global light_time,lightning
    light_time += gfw.delta_time
    if light_time > random.uniform(3.0,4.0):
        lightning = 160
        light_time = 0

    if lightning- 3 >= 0:
        lightning -= 3
    SDL_SetTextureAlphaMod(light.texture,lightning)
        
def highlightButton():
    global Sbutton,Rbutton,Qbutton,Smag,Rmag,Qmag
    if selected == 3:
        if Smag + 0.02 < 1.5:
            Smag += 0.02
        if Rmag - 0.05 > 1.0:
            Rmag -= 0.05
        if Qmag - 0.05 > 1.0:
            Qmag -= 0.05
    elif selected ==  2:
        if Smag - 0.05 > 1.0:
            Smag -= 0.05
        if Rmag + 0.02 < 1.5:
            Rmag += 0.02
        if Qmag - 0.05 > 1.0:
            Qmag -= 0.05
    elif selected == 1:
        if Smag - 0.05 > 1.0:
            Smag -= 0.05
        if Rmag - 0.05 > 1.0:
            Rmag -= 0.05
        if Qmag + 0.02 < 1.5:
            Qmag += 0.02



def update():
    gfw.world.update()
    lightfunc()
    highlightButton()
    check()

def check():
    pass

    

def draw():
    bg.draw(320,240)
    light.draw(320,240)
    name.draw(320,340)
    if selected == 1:
        start.draw(320,190,start.w*Smag,start.h*Smag)
        rank.draw(320,120,rank.w*Rmag,rank.h*Rmag)
        mquit.draw(320,50,mquit.w*Qmag,mquit.h*Qmag)
    elif selected == 2:
        start.draw(320,190,start.w*Smag,start.h*Smag)
        mquit.draw(320,50,mquit.w*Qmag,mquit.h*Qmag)
        rank.draw(320,120,rank.w*Rmag,rank.h*Rmag)
    elif selected == 3:
        rank.draw(320,120,rank.w*Rmag,rank.h*Rmag)
        mquit.draw(320,50,mquit.w*Qmag,mquit.h*Qmag)
        start.draw(320,190,start.w*Smag,start.h*Smag)


    select.draw(320,selecty)
    
    
    mfont.draw(canvas_width-155,canvas_height-10,"Arrow keys (Select)",(230,230,230))
    mfont.draw(canvas_width-115,canvas_height-25,"Enter (Choose)",(230,230,230))
    
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
            if selected == 1:
                gfw.pop()

def resume():
    gfw.world.init([])

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()

