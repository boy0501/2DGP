import gfw
from pico2d import *
import gobj
import main_state
import start_state
import random
import highscore


canvas_width = 640
canvas_height = 480

def enter():
    gfw.world.init([])
    highscore.load()
    global bg,mpause,light,main,rank,mquit,select,back
    bg = gfw.image.load('./res/bg/722.png')
    mpause = gfw.image.load('./res/bg/Pause.png')
    light = gfw.image.load('./res/bg/89.png')
    main = gfw.image.load('./res/bg/Main.png')
    back = gfw.image.load('./res/bg/Back.png')
    rank = gfw.image.load('./res/bg/Rank.png')
    mquit = gfw.image.load('./res/bg/Quit.png')
    select = gfw.image.load('./res/bg/1270.png')
    global lightning,light_time
    lightning = 0
    light_time = 0
    
    global text
    text = ''   
    global selecty,selected
    selecty = 50
    selected = 4
    
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
        
def update():
    gfw.world.update()
    lightfunc()
    check()

def check():
    pass

    

def draw():
    bg.draw(320,240,bg.w,bg.h*0.3)
    light.draw(320,240)
    rank.draw(320,400)
    highscore.draw()
    back.draw(320,50)
    select.draw(150,selecty)
    
    
    mfont.draw(canvas_width-155,canvas_height-10,"Arrow keys (Select)",(230,230,230))
    mfont.draw(canvas_width-115,canvas_height-25,"Enter (Choose)",(230,230,230))
    
    gfw.world.draw()

def pause():    
    pass

def handle_event(e):
    global selecty,selected,text
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:
            gfw.pop()
        elif e.key == None:
            pass
        elif 32<=int(e.key) and e.key<=int(126):
            text += chr(e.key)
            print(text)
        else :
            print(e.key)

def resume():
    gfw.world.init([])

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()


