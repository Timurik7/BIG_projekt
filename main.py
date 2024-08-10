from setings import *

game = True


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()



    if game:
        ...


    pygame.display.update()
    clock.tick(fps)