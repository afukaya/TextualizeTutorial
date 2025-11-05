# Define a minimal user interface application with textual.

from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer

class HelloApp(App):
# Base textual application class. This is the textual application entry point.
# This class will hold all the user interface objects.

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()


# Call the application.
if __name__ == "__main__":
    HelloApp().run()