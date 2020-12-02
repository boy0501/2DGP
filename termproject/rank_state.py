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
    
    global text
    text = ''   
    global selecty,selected
    selecty = 50
    selected = 4
    
    global mfont
    mfont = gfw.font.load('./res/ConsolaMalgun.ttf',15)
    global rank_music
    rank_music = load_wav('./res/미싱노브금/select.wav')
    rank_music.set_volume(30)
    rank_music.repeat_play()

        
def update():
    gfw.world.update()
    check()

def check():
    pass

    

def draw():
    bg.draw(320,240,bg.w,bg.h*0.3)
    rank.draw(320,400)
    highscore.draw()
    back.draw(320,50)
    select.draw(150,selecty)
    
    mfont.draw(30,canvas_height-10,"In game",(230,230,230))
    mfont.draw(0,canvas_height-25,"(Move) Arrow keys",(230,230,230))
    mfont.draw(0,canvas_height-40,"(jump) Left Shift",(230,230,230))
    mfont.draw(0,canvas_height-55,"(attack) z",(230,230,230))
    mfont.draw(canvas_width-100,canvas_height-10,"In menu",(230,230,230))
    mfont.draw(canvas_width-155,canvas_height-25,"Arrow keys (Select)",(230,230,230))
    mfont.draw(canvas_width-115,canvas_height-40,"Enter (Choose)",(230,230,230))
    
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

def resume():
    gfw.world.init([])

def exit():
    global rank_music
    del rank_music


if __name__ == '__main__':
    gfw.run_main()


