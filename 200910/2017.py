from pico2d import*

open_canvas()
img = load_image('../res/run_animation.png')
gra = load_image('../res/grass.png')

gra.draw_now(400,30)

x = 0
frame = 0
while x< 800:
    clear_canvas()
    gra.draw(400,30)
    img.clip_draw(frame*100,0,100,100,x,85)
    update_canvas()
    
    get_events()
    x+=2
    frame += 1
    if frame >= 8: frame = 0
    delay(0.01)

delay(5)
