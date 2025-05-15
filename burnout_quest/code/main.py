# main.py
import pygame
import sys
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = TITLE_SCREEN
        self.font = pygame.font.Font(None, 36)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_SPACE:
                    if self.state == TITLE_SCREEN:
                        print("Game would transition here to character creation...")

    def update(self):
        pass  # Game logic updates go here

    def render(self):
        self.screen.fill(BLACK)
        if self.state == TITLE_SCREEN:
            self.draw_title_screen()

    def draw_title_screen(self):
        title = self.font.render(TITLE, True, WHITE)
        subtitle = self.font.render("A Satirical 8-Bit JRPG About Modern Tech Life", True, WHITE)
        start = self.font.render("Press SPACE to Start", True, WHITE)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        self.screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 3 + 50))
        self.screen.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT // 3 + 150))

if __name__ == '__main__':
    game = Game()
    game.run()
