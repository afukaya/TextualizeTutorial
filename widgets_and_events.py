from textual.app import App
from textual.containers import Vertical
from textual.widgets import Header, Footer, Static, Button

class TextApp(App):
    
    CSS_PATH = 'widgets_and_events.tcss'

    def compose(self):
        yield Header(show_clock=True)
        with Vertical():
            yield Static('Widgets and Events', id="title")
            yield Button('Click Me', id="click_button")    
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "click_button":
            self.query_one("#title", Static).update("Button Clicked!")

if __name__ == '__main__':
    TextApp().run()