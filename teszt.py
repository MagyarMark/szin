import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1020,610))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

#sky_surface = pygame.image.load('kezdo.jpg')

TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

font = pygame.font.SysFont("arialblack", 40)

game_paused = False

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_passed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if pygame.mouse.get_passed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))

    





while True:
    if game_paused == True:
        pass
    else:
        draw_text("Nyomd meg a SPACE-t hogy megálitsd", font, TEXT_COL, 160, 250)
    


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(sky_surface,(0,0))

    pygame.display.update()
    clock.tick(60)