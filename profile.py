import json
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from datetime import datetime
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock



class Profile(Screen):

    def information_func(self):
        pass


    def spinner_func(self):
        pass

class Quests(Screen):
    pass

class Completion(Screen):
    pass


class CircularProgressBar(ProgressBar):

    def __init__(self, *args, **kwargs):
        super(CircularProgressBar, self).__init__(*args, **kwargs)

        # Set constant for the bar thickness
        self.thickness = 40

        # Create a direct text representation
        self.label = CoreLabel(text="0%", font_size=self.thickness)

        # Initialise the texture_size variable
        #self.texture_size = None

        # Refresh the text
        self.refresh_text()

        # Redraw on innit
        self.draw()

    def draw(self):

        with self.canvas:

            # Empty canvas instructions
            self.canvas.clear()

            # Draw no-progress circle
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=self.pos, size=self.size)

            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
            Color(1, 0, 0)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized*360))

            # Draw the inner circle (colour should be equal to the background)
            Color(0, 0, 0)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))

            # Center and draw the progress text
            Color(1, 1, 1, 1)
            Rectangle(texture=self.label.texture, size=self.texture_size,
                      pos=(self.size[0]/2 - self.texture_size[0]/2, self.size[1]/2 - self.texture_size[1]/2))

    def refresh_text(self):
        # Render the label
        self.label.refresh()

        # Set the texture size each refresh
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        # Update the progress bar value
        self.value = value

        # Update textual value and refresh the texture
        self.label.text = str(int(self.value_normalized*100)) + "%"
        self.refresh_text()

        # Draw all the elements
        self.draw()

def main():
    pass


class managerApp(App):
    pass


class ProfileApp(App):
    def build(self):
        self.root = Builder.load_file('profile.kv')
        return Profile()

if __name__ == '__main__':
    #ProfileApp().run()
    managerApp().run()
