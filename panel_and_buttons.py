# Define a minimal user interface application with textual.

from textual.app import App
from textual.containers import Horizontal,Vertical, Grid
from textual.widgets import Button, Header, Footer, Static

class HelloApp(App):
# Base textual application class. This is the textual application entry point.
# This class will hold all the user interface objects.
    CSS_PATH = "panel_and_buttons.tcss"

    def compose(self):
        yield Header(show_clock=True)
        with Horizontal(id="Main-Panel"):
            yield Static("Horizontal Panel", id="main-panel-text")
            with Vertical(id="Vertical-Panel"):
                yield Static("Vertical Panel"  , id="vertical-panel-text")
                yield Button("Button 1", id="button1", classes="vertical-button")
                yield Button("Button 2", id="button2", classes="vertical-button")
                yield Button("Button 3", id="button3", classes="vertical-button")
            
            with Grid(id="Grid-Panel"):
                yield Static("Grid Panel", id="grid-panel-text")
                yield Button("Button 4", id="button4", classes="grid-button")
                yield Button("Button 5", id="button5", classes="grid-button")
                yield Button("Button 6", id="button6", classes="grid-button")
                yield Button("Button 7", id="button7", classes="grid-button")
                yield Button("Button 8", id="button8", classes="grid-button")
        
            yield Button("Sair", id="button-quit", classes="main-button")
        
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "button-quit":
            self.exit()
    


# Call the application.
if __name__ == "__main__":
    HelloApp().run()