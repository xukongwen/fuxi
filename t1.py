import pygame
from pygame.locals import *
pygame.init()

import pygame as pg


def title():
    clock = pg.time.Clock()
    screen = pygame.display.set_mode((1395, 855), pygame.FULLSCREEN)
    font = pygame.font.Font("KKong3.ttf", 70)
    
    color = pg.Color('#FFFFFF')
    orig_surf = font.render("Filler: ", True, color)
    color2 = pg.Color('#FFFFFF')
    orig2_surf = font.render("Very Cool", True, color2)
    
    txt_surf = orig_surf.copy()
    txt2_surf = orig2_surf.copy()
    alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
    alpha2_surf = pg.Surface(txt2_surf.get_size(), pg.SRCALPHA)
    
    alpha = 255
    counter = 0

    while True:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.mixer.music.fadeout(1000)
                return

        if alpha > 0 and counter <= 80:
            alpha = max(alpha-0, 0)
            txt_surf = orig_surf.copy()
            alpha_surf.fill((255, 255, 255, alpha))
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
            
            txt2_surf = orig2_surf.copy()
            alpha2_surf.fill((255, 255, 255, alpha))
            txt2_surf.blit(alpha2_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
            
            counter += 1
            
        elif alpha > 0 and counter > 80:
            alpha = max(alpha-1.2, 0)
            txt_surf = orig_surf.copy()
            alpha_surf.fill((255, 255, 255, alpha))
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

            txt2_surf = orig2_surf.copy()
            alpha2_surf.fill((255, 255, 255, alpha))
            txt2_surf.blit(alpha2_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)



        #screen.fill((9, 47, 68, alpha))
        screen.fill((0, 66, 99, alpha))
        
        screen.blit(txt_surf, (302, 348))
        screen.blit(txt2_surf, (509, 418))

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    title()
    pg.quit()