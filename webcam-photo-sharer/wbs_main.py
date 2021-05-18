from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from filestack import Client
import time
import webbrowser
import os
from dotenv import load_dotenv
load_dotenv()


Builder.load_file("wbs_front.kv")


class CameraScreen(Screen):

    def start(self):
        # Starts the camera and changes the Button text.
        self.ids.camera.play = True
        self.ids.camera.opacity = 1
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        # Stops the camera and changes the Button text.
        self.ids.camera.play = False
        self.ids.camera.opacity = 0
        self.ids.camera.texture = None

    def capture(self):
        # Creates a filename with the current time and captures and saves a screen under that filename.
        self.filepath = "files/" + time.strftime("%Y%m%d-%H%M%S") + ".png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "photo_screen"
        self.manager.current_screen.ids.screen.source = self.filepath


class PhotoScreen(Screen):

    link_message = "Create a link first!"

    def create_link(self):
        # Accesses the screen filepath, uploads it to the web and inserts the link into the Label widget.
        image_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath=image_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        # Copies the link to the clipboard.
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        # Opens the link with a default browser.
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class FileSharer:

    def __init__(self, filepath, api_key=os.environ["FILESTACK_API_KEY"]):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_link = client.upload(filepath=self.filepath)
        return new_link.url


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
