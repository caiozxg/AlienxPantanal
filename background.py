from StaticSprite import StaticSprite

class Background(StaticSprite):
    def __init__(self,image,position,horizontal_speed):
        super().__init__(image,position)
        self.horizontal_speed = horizontal_speed
    
    def update(self,dt):
        self.rect.x -= self.horizontal_speed * dt

