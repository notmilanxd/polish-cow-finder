import pygame
import pygame_gui
import random


pygame.init()

screenWidth = 800
screenHeight = 600

randomWidth = random.randrange(screenWidth-50)
randomHeight = random.randrange(screenHeight-50)

pygame.display.set_caption("cow")
screen = pygame.display.set_mode((screenWidth, screenHeight))

manager = pygame_gui.UIManager((800, 600))

clock = pygame.time.Clock()



cow = pygame.Rect((randomWidth, randomHeight, 50, 50))


pygame.mixer.init
polishCow = pygame.mixer.Sound("./polishcow.mp3")

mooCow = pygame.mixer.Sound("./cowsound.mp3")

img = pygame.image.load('R.gif')

print(f"{randomWidth}, {randomHeight}")

run = True
isMusicPlaying = True
mouseCheck = True

while run:
    
    
    screen.fill((255, 255, 255))

    if isMusicPlaying == True:
        polishCow.play(-1)
    
    pygame.draw.rect(screen, (255, 255, 0), cow)

    mouseX, mouseY = pygame.mouse.get_pos()

    if cow.collidepoint((mouseX, mouseY)) and mouseCheck == True:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
   
    
    volumeMath = pygame.math.Vector2(mouseX, mouseY).distance_to((randomWidth, randomHeight))
    
    if 10/volumeMath != 0:
        polishCow.set_volume(10/volumeMath)

    time_delta = clock.tick()


    for event in pygame.event.get():
        

        manager.process_events(event)

        manager.update(time_delta)

        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if cow.collidepoint((mouseX, mouseY)) and mouseCheck == True:
                
                mouseCheck = False
                isMusicPlaying = False
                polishCow.stop()
                mooCow.play()
                hello_button = pygame_gui.elements.UITextBox(html_text="<b>You have found Polish cow!</b>", relative_rect=pygame.Rect(300, 200, 250, 70))

        
        if event.type == pygame.QUIT:
            run = False

    manager.draw_ui(screen)
    
    pygame.display.update()

pygame.quit()