import gfw
from pico2d import *
from player import Player
from bullet import Bullet
from boss import Boss
from background import Background
import gobj
import pause_state
import start_state
import highscore
import record


canvas_width = 640
canvas_height = 480

MAX_objects = 11 

def enter():
    gfw.world.init(['bg', 'bullet','player','boss','rock','beam','leaf','blood','text','die','boss_die_effect'])
    global player
    global boss
    global diebg
    global textbg
    global bg
    global game_over
    global to_pause
    global clear_time,clear_flag,name
    record.load()
    name = 'no_name'
    clear_time = 0
    clear_flag = 0
    to_pause = {}
    game_over = False
    player = Player()
    boss = Boss()
    bg = Background()
    diebg = Background(1)
    textbg = Background(2)
    gfw.world.add(gfw.layer.text,textbg)
    gfw.world.add(gfw.layer.player, player)
    gfw.world.add(gfw.layer.die,diebg)
    gfw.world.add(gfw.layer.bg, bg)
    gfw.world.add(gfw.layer.boss,boss)

def update():
    global clear_time
    if boss.get_boss_die() == 0:
        clear_time += gfw.delta_time
    gfw.world.update()
    check()
    #print(gfw.delta_time)

def check():
    global game_over,clear_flag,clear_time
    if gobj.collides_box(player,boss):
        pass

    for bullet in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(bullet, boss):
            gfw.world.remove(bullet)
            Bullet.BULLET_NUM-=1
            boss.hit()
    
    for pattern in gfw.world.objects_at(gfw.layer.rock):
        if player.die_value == 0:
            if gobj.collides_box(player,pattern):
                player.die()
                diebg.set_death_img_to_die()
                print("당신은 죽었습니다")

    for pattern in gfw.world.objects_at(gfw.layer.beam):
        if player.die_value == 0:
            if gobj.collides_box(player,pattern):
                player.die()
                diebg.set_death_img_to_die()
                print("당신은 죽었습니다")
    for pattern in gfw.world.objects_at(gfw.layer.leaf):
        if player.die_value == 0:
            if gobj.collides_box(player,pattern):
                player.die()
                diebg.set_death_img_to_die()
                print("당신은 죽었습니다")
    if game_over == False:
        if player.get_die_value() ==1:
            player.die()
            diebg.set_death_img_to_die()
            print("당신은 죽었습니다")    
            game_over = True   
    if boss.get_boss_die() != 0 :
        if clear_flag == 0:
            clear_flag = 1

    #if gobj.collides_box(,boss):
    #    print('bullet')

    

def draw():
    gfw.world.draw()
    if boss.get_boss_die() != 0:
        record.draw(name)
    #gobj.draw_collision_box()

def pause():
    global to_pause

    for i in range(MAX_objects):
        to_list = []
        for obj in gfw.world.objects_at(i):
            to_list.append(obj)
        to_pause[i] = to_list

        

def resume():
    gfw.world.init(['bg', 'bullet','player','boss','rock','beam','leaf','blood','text','die','boss_die_effect'])
    global to_pause
    
    for i in range(MAX_objects):
        for obj in to_pause[i]:
            gfw.world.add(i,obj)
 



def handle_event(e):
    global player,name,clear_time
    # prev_dx = boy.dx

    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if boss.get_boss_die() != 0:
            if e.key != None:
                if 32<=int(e.key) and e.key<=int(126):
                    if len(name) < 13:
                        name += chr(e.key)
                elif e.key == SDLK_BACKSPACE:
                    name = name[:-1]
                elif e.key == SDLK_RETURN:
                    highscore.load()
                    highscore.add(clear_time,name)
                    highscore.save()
                    gfw.change(start_state)
                    clear_time = 0
        elif e.key == SDLK_ESCAPE:
            gfw.push(pause_state)
        elif e.key == SDLK_r:
            if player.die_value == 1:
                gfw.change(start_state)
    player.handle_event(e)



def exit():
    return

if __name__ == '__main__':
    gfw.run_main()


