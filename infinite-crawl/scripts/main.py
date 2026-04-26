import pygame
import sys
from player import Player

#Constants
WIDTH = 800
HEIGHT = 450
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Infinite Crawl")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 30)
        self.player = Player((WIDTH/2, HEIGHT/2))


    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.player.update(dt, events)
            self.screen.fill("black")
            self.player.draw(self.screen)
            fps = str(int(self.clock.get_fps()))
            fps_surface = self.font.render(fps, True, 'white')
            self.screen.blit(fps_surface, (10,10))
            pygame.display.update()


if __name__=="__main__":
    game = Game()  
    game.run()