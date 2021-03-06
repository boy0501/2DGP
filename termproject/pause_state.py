import gfw
from pico2d import *
import gobj
import main_state
import start_state
import rank_state
import random


canvas_width = 640
canvas_height = 480

def enter():
    gfw.world.init([])

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
    
    global selecty,selected
    selecty = 300
    selected = 4
    
    global Bmag,Mmag,Rmag,Qmag
    Bmag = Mmag = Rmag = Qmag = 1

    global mfont
    mfont = gfw.font.load('./res/ConsolaMalgun.ttf',15)

    global pause_music
    pause_music = load_wav('./res/미싱노브금/relax.wav')
    pause_music.set_volume(40)
    pause_music.repeat_play()
    
        
def highlightButton():
    global Bmag,Mmag,Rmag,Qmag
    if selected == 4:
        if Bmag + 0.02 <1.5:
            Bmag += 0.02
        if Mmag - 0.05 > 1.0:
            Mmag -= 0.05
        if Rmag - 0.05 > 1.0:
            Rmag -= 0.05
        if Qmag - 0.05 > 1.0:
            Qmag -= 0.05        
    elif selected == 3:
        if Bmag - 0.05 > 1.0:
            Bmag -= 0.05        
        if Mmag + 0.02 < 1.5:
            Mmag += 0.02
        if Rmag - 0.05 > 1.0:
            Rmag -= 0.05
        if Qmag - 0.05 > 1.0:
            Qmag -= 0.05
    elif selected ==  2:
        if Bmag - 0.05 >1.0:
            Bmag -= 0.05 
        if Mmag - 0.05 > 1.0:
            Mmag -= 0.05
        if Rmag + 0.02 < 1.5:
            Rmag += 0.02
        if Qmag - 0.05 > 1.0:
            Qmag -= 0.05
    elif selected == 1:
        if Bmag - 0.05 >1.0:
            Bmag -= 0.05 
        if Mmag - 0.05 > 1.0:
            Mmag -= 0.05
        if Rmag - 0.05 > 1.0:
            Rmag -= 0.05
        if Qmag + 0.02 < 1.5:
            Qmag += 0.02



def update():
    gfw.world.update()
    highlightButton()
    check()

def check():
    pass

    

def draw():
    bg.draw(320,240,bg.w,bg.h*0.3)
    mpause.draw(320,400)
    if selected == 1:
        back.draw(320,300,back.w*Bmag,back.h*Bmag)
        main.draw(320,230,main.w*Mmag,main.h*Mmag)
        rank.draw(320,160,rank.w*Rmag,rank.h*Rmag)
        mquit.draw(320,90,mquit.w*Qmag,mquit.h*Qmag)
    elif selected == 2:
        back.draw(320,300,back.w*Bmag,back.h*Bmag)
        mquit.draw(320,90,mquit.w*Qmag,mquit.h*Qmag)
        main.draw(320,230,main.w*Mmag,main.h*Mmag)
        rank.draw(320,160,rank.w*Rmag,rank.h*Rmag)
    elif selected == 3:
        back.draw(320,300,back.w*Bmag,back.h*Bmag)
        mquit.draw(320,90,mquit.w*Qmag,mquit.h*Qmag)
        rank.draw(320,160,rank.w*Rmag,rank.h*Rmag)
        main.draw(320,230,main.w*Mmag,main.h*Mmag)
    elif selected == 4:
        mquit.draw(320,90,mquit.w*Qmag,mquit.h*Qmag)
        rank.draw(320,160,rank.w*Rmag,rank.h*Rmag)
        main.draw(320,230,main.w*Mmag,main.h*Mmag)
        back.draw(320,300,back.w*Bmag,back.h*Bmag)


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
    global pause_music
    del pause_music

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
            if selecty + 70 <=310:
                selecty += 70
                selected += 1
        elif e.key == SDLK_RETURN:
            if selected == 4:
                gfw.pop()
            elif selected == 3:
                gfw.change(start_state)
            elif selected == 2:
                gfw.push(rank_state)
            elif selected == 1:
                gfw.quit()

def resume():
    gfw.world.init([])
    global pause_music
    pause_music = load_wav('./res/미싱노브금/relax.wav')
    pause_music.set_volume(40)
    pause_music.repeat_play()

def exit():
    global pause_music
    del pause_music

if __name__ == '__main__':
    gfw.run_main()


