from scamp import *
def play_piano():
    s=Session()
    piano=s.new_part("Piano")
    import pygame
    pygame.init()
    win=pygame.display.set_mode((500,500))
    run=True
    x=50
    y=50
    width=40
    height=60
    vel=5
    button = pygame.draw.rect(win,(150,0,0),(150,150,50,50))
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    piano.play_note(440,1,2)
        keys =pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y-=vel
        if keys[pygame.K_s]:
            y+=vel
        if keys[pygame.K_a]:
            x-=vel
        if keys[pygame.K_d]:
            x+=vel
        pygame.draw.rect(win,(110,110,110),(x,y,width,height))
        pygame.display.update()

    pygame.quit()
