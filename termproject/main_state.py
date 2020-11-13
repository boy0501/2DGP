import gfw
from pico2d import *
from player import Player
from bullet import Bullet
from boss import Boss
from background import Background
import gobj


canvas_width = 640
canvas_height = 480

def enter():
    gfw.world.init(['bg', 'bullet','player','boss','rock','beam','leaf','blood','die'])
    global player
    global boss
    global diebg
    player = Player()
    boss = Boss()
    bg = Background()
    diebg = Background(1)
    gfw.world.add(gfw.layer.player, player)
    gfw.world.add(gfw.layer.die,diebg)
    gfw.world.add(gfw.layer.bg, bg)
    gfw.world.add(gfw.layer.boss,boss)

def update():
    gfw.world.update()
    check()
    #print(gfw.delta_time)

def check():
    if gobj.collides_box(player,boss):
        pass

    for bullet in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(bullet, boss):
            gfw.world.remove(bullet)
            Bullet.BULLET_NUM-=1
    
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
    #if gobj.collides_box(,boss):
    #    print('bullet')

    

def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()


def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()


