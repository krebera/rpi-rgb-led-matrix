from bikeloadingbar import BikeLoadingBar
from app_class import App, AppType
from strava_api import get_strava_data
import asyncio

class Strava(App):

    def __init__(self):
        super(Strava, self).__init__()
        self.app_type = AppType.STRAVA
        self.currentView = None
        self.loading_bar_counter = 0
        self.switch(0)
        
    def update(self):
        if(self.state == 0):
            self.currentView.render(self.loading_bar_counter)
        else:
            self.currentView.render()
    
    def switch(self, new_state):
        if(new_state == 0):
            self.currentView = BikeLoadingBar()
            self.state = new_state
        else:
            self.state = new_state