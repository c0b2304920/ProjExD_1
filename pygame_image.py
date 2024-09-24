import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    bg2_img = pg.transform.flip(bg_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    tmr = 0
    kk_r = kk_img.get_rect()
    kk_r.center = 300,200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            kk_r.move_ip((0,-3))
        if key_list[pg.K_DOWN]:
            kk_r.move_ip((0,3))
        if key_list[pg.K_LEFT]:
            kk_r.move_ip((-3,0))
        if key_list[pg.K_RIGHT]:
            kk_r.move_ip((3,0))
        x=-(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg2_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg2_img, [x+4800, 0])
        screen.blit(kk_img, kk_r)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()