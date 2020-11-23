import gfw
from pico2d import *
from player import Player
from bullet import Bullet
from boss import Boss
from background import Background
import gobj
import pause_state
import start_state


canvas_width = 640
canvas_height = 480

def enter():
    gfw.world.init(['bg', 'bullet','player','boss','rock','beam','leaf','blood','text','die'])
    global player
    global boss
    global diebg
    global textbg
    global bg
    global game_over
    global to_pause
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
    gfw.world.update()
    check()
    #print(gfw.delta_time)

def check():
    global game_over
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
    #if gobj.collides_box(,boss):
    #    print('bullet')

    

def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()

def pause():
    global to_pause

    for i in range(10):
        to_list = []
        if i == 0:
            for obj in gfw.world.objects_at(gfw.layer.bg):
                to_list.append(obj)
        elif i == 1:
            for obj in gfw.world.objects_at(gfw.layer.bullet):
                to_list.append(obj)    
        elif i == 2:
            for obj in gfw.world.objects_at(gfw.layer.player):
                to_list.append(obj)     
        elif i == 3:
            for obj in gfw.world.objects_at(gfw.layer.boss):
                to_list.append(obj)                
        elif i == 4:
            for obj in gfw.world.objects_at(gfw.layer.rock):
                to_list.append(obj)    
        elif i == 5:
            for obj in gfw.world.objects_at(gfw.layer.beam):
                to_list.append(obj)                    
        elif i == 6:
            for obj in gfw.world.objects_at(gfw.layer.leaf):
                to_list.append(obj)                    
        elif i == 7:
            for obj in gfw.world.objects_at(gfw.layer.blood):
                to_list.append(obj)                   
        elif i == 8:
            for obj in gfw.world.objects_at(gfw.layer.text):
                to_list.append(obj)                    
        elif i == 9:
            for obj in gfw.world.objects_at(gfw.layer.die):
                to_list.append(obj)                   
     
        to_pause[i] = to_list
        

def resume():
    gfw.world.init(['bg', 'bullet','player','boss','rock','beam','leaf','blood','text','die'])
    global to_pause
    
    for i in range(10):
        if i == 0:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.bg,obj)
        elif i == 1:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.bullet,obj)   
        elif i == 2:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.player,obj)      
        elif i == 3:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.boss,obj)                  
        elif i == 4:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.rock,obj)     
        elif i == 5:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.beam,obj)                     
        elif i == 6:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.leaf,obj)                      
        elif i == 7:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.blood,obj)                  
        elif i == 8:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.text,obj)                     
        elif i == 9:
            for obj in to_pause[i]:
                gfw.world.add(gfw.layer.die,obj)      





def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.push(pause_state)
        elif e.key == SDLK_r:
            if player.die_value == 1:
                gfw.change(start_state)


    player.handle_event(e)

def exit():
    return

if __name__ == '__main__':
    gfw.run_main()


