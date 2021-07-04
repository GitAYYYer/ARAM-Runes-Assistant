import pygame

class Button(object):
    def __init__(self, img, position, size):
        # load image onto button
        self.img = pygame.image.load(img)
        self.img.convert()
        self.img = pygame.transform.rotozoom(self.img, 0, 0.5)

        # get image size and position
        self.rect = pygame.Rect(position, size)


    def draw(self, screen):
        # draw selected image
        screen.blit(self.img, self.rect)

    def eventHandler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self.rect.collidepoint(event.pos): # is mouse over button
                    return str("Aurelion Sol").lower()
