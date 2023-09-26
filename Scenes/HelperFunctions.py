import pygame
from pygame.locals import MOUSEBUTTONDOWN


def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    while words:
        line = ''
        while words and font.size(line + words[0])[0] <= max_width:
            line += (words.pop(0) + ' ')
        surface = font.render(line, True, (255, 255, 255))
        lines.append(surface)
    return lines

def textbox():
    pass


class Button:
    def __init__(self, text, x, y, w, h, color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surf = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()
