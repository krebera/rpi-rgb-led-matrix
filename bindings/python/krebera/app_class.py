from enum import Enum
import asyncio

class AppType(Enum):
    STRAVA = 1
    POKEMON = 2

class App():
    # Matrix hopefully passed down from manager
    def __init__(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def dismiss(self):
        pass