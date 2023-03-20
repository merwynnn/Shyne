import pygame
pygame.init()
small_font = pygame.font.SysFont('arial', 25)

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Shyne')
clock = pygame.time.Clock()
tags = {}




while True:

    dt = clock.tick()

    fps = int(clock.get_fps())
    events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()

    win.fill((255, 255, 255))


    fps_txt = small_font.render(str(fps), True, (0, 0, 255))
    win.blit(fps_txt, (10, 10))
    pygame.display.update()
