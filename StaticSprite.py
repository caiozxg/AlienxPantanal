import pygame


class StaticSprite(pygame.sprite.Sprite):
    def __init__(self,image,position):

        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(midbottom = position)
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    
    def update(self,dt):
        self.rect -= self.horizontal_speed * dt


    


    

        
        