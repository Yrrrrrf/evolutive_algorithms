from enum import Enum


class Config(Enum):
    """
    Application configuration
    """
    NAME: str = "Evolutive Alrogithms"
    VERSION: str = "v0.1.0"
    
    # App settings
    WIDTH: int = 720
    HEIGHT: int = 480
    FPS = 60  # frames per second
    TILE_SIZE = 128
    GAME_SIZE = 3


class Theme(Enum):
    """
    App main colors
    """
    # Colors
    BACKGROUND: tuple = (32, 32, 32)

    # Fonts

