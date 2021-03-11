import pygame


class Ship():# класс для управления кораблем
    def __init__(self, ai_game):
        # Инициализаруем корабль и задаем его начальную позицию
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружаем изображение корабля и получаем прямоугольник
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        
        # Появление каждого нового корабля у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

