import pygame

class Animation:
    """
    A list of frames
    """

    def add(self, path):
        """
        Adds an image to the list
        """
        self.frame.append(pygame.image.load(path).convert_alpha())
        return self

    def __init__(self, fps = 15):
        """
        Initializes an empty list
        """
        self.frame = []
        self.fps = fps
