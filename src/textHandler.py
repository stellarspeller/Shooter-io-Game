#is interacted with by run.py, uses pygame to create a text box

from src.constants import *
class textHandler:
    def __init__(self, text, font, pos, color, delay=False, fade_duration=0, lifetime=float('inf')):
        self.text = text
        self.font = font
        self.pos = pos
        self.color = color # background color of the text
        self.alpha = 255  # Initial alpha value
        self.fade_duration = fade_duration  # Duration of fade-out in seconds
        self.lifetime = lifetime  # Total lifetime of the text in seconds
        self.start_time = pygame.time.get_ticks()  # Start time of the text
        self.delay = delay

    def get_width(self):
        return self.font.render(self.text, True, self.color).get_width()
    
    def get_height(self):
        return self.font.render(self.text, True, self.color).get_height()

    def kill(self):
        textList.remove(self)

    def render(self):
        # Render the text with the current alpha value
        text_surface = self.font.render(self.text, True, self.color)
        text_surface.set_alpha(self.alpha)
        screen.blit(text_surface, self.pos)

    def update(self):
        # Skip the elapsed time check if the text is meant to last forever
        if not self.delay:
            return
        
        print(self.fade_duration)
        print(self.lifetime)

        # Calculate the current time since the text was created
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / 1000.0

        # Check if the text has reached its lifetime
        if elapsed_time >= self.lifetime:
            #textList.remove(self)
            self.kill()
            return

        # Calculate the current alpha value based on the elapsed time
        # utilize alpha * 255, where alpha is some number 0-1 for time between fade_duration and lifetime
        # and where alpha is greater than 1 (and thus set to 1) for time between 0 and lifetime-fadeduration

        if elapsed_time <= self.lifetime - self.fade_duration:
            self.alpha = 255
        else:
            self.alpha = 255 * (1 - (elapsed_time - (self.lifetime - self.fade_duration)) / self.fade_duration)


