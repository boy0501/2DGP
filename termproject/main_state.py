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
    global cheat_key,cheat_name,cheat_active
    cheat_key = False
    cheat_name = ''
    cheat_active = False
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

    global main_music,appear_m
    main_music = load_music('./res/미싱노브금/Pokemon_Battle_Megamix.ogg')
    main_music.set_volume(40)
    main_music.repeat_play()
    appear_m = load_wav('./res/미싱노브금/rattata.wav')
    appear_m.set_volume(20)
    appear_m.play()

def update():
    global clear_time
    if boss.get_boss_die() == 0:
        clear_time += gfw.delta_time
    gfw.world.update()
    check()
    #print(gfw.delta_time)


def check():
    global game_over,clear_flag,clear_time       

    for bullet in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(bullet, boss):
            gfw.world.remove(bullet)
            Bullet.BULLET_NUM-=1
            if boss.get_shield() == False:
                boss.hit()
            else :
                boss.set_shield_alpha()


    if cheat_active == False:
        if gobj.collides_box(player,boss):
            if player.die_value == 0:
                player.die()
                diebg.set_death_img_to_die()
                print("당신은 죽었습니다")    

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
    gobj.draw_collision_box()
    
    

def pause():
    global to_pause

    for i in range(MAX_objects):
        to_list = []
        for obj in gfw.world.objects_at(i):
            to_list.append(obj)
        to_pause[i] = to_list

    player.reset_to_bug_solve_IS_UPKEYPRESSED()
    print(main_music)
    main_music.pause()

        

def resume():
    gfw.world.init(['bg', 'bullet','player','boss','rock','beam','leaf','blood','text','die','boss_die_effect'])
    global to_pause
    
    for i in range(MAX_objects):
        for obj in to_pause[i]:
            gfw.world.add(i,obj)
    
    main_music.resume()
    print(main_music)

def check_cheat():
    global cheat_name,cheat_active
    if cheat_name == 'shield':
        cheat_active = True
        for text in gfw.world.objects_at(gfw.layer.text):
                    text.set_text(text.TEXT_DIC['Cheat'])    #text는 textbg를 objects_at 해오는거고, 이 객체에는 TEXT_DIC이라는





def handle_event(e):
    global player,name,clear_time
    global cheat_key,cheat_name

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
        elif e.key == SDLK_1:
            cheat_key = True
        elif cheat_key == True:
            if e.key != None:
                if 32<=int(e.key) and e.key<=int(126):
                    cheat_name += chr(e.key)
                elif e.key == SDLK_RETURN:
                    check_cheat()


    elif e.type == SDL_KEYUP:
        if e.key == SDLK_1:
            cheat_key = False
    player.handle_event(e)



def exit():
    #player.reset_to_bug_solve_IS_UPKEYPRESSED()
    return

if __name__ == '__main__':
    gfw.run_main()


