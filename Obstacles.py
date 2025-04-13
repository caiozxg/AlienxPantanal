from StaticSprite import StaticSprite

class Obstacle(StaticSprite):
    def __init__(self, image, position,horizontal_speed):
        super().__init__(image, position)
        self.horizontal_speed = horizontal_speed
        self.hitbox_rect = self.rect.inflate(-20,-20)   #diminui um pouco o tamanho do retangulo de colisao, mantendo o centro
    def update(self,dt):
        super().update(dt)
        self.hitbox_rect.center = self.rect.center
        
