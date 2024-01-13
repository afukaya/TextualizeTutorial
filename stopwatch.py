from time import monotonic
from textual import on
from textual.app import App
from textual.widgets import Header, Footer, Static, Button
from textual.reactive import reactive
from textual.containers import ScrollableContainer

class TimeDisplay(Static):
    
    time = reactive(0)
    time_start = reactive(monotonic())
    time_total = reactive(0)

    def on_mount(self):
        self.update_timer = self.set_interval(1/60,self.update_time,pause=True)

    def update_time(self):
        self.time = self.time_total + (monotonic() - self.time_start)

    def watch_time(self):
        time = self.time
        minutes, seconds = divmod(time,60)
        hours, minutes = divmod(minutes,60)
        self.update(f"{hours:02,.0f}:{minutes:02,.0f}:{seconds:05.2f}")

    def start(self):
        self.time_start = monotonic()
        self.update_timer.resume()
    
    def stop(self):
        self.update_timer.pause()
        self.time_total += monotonic() - self.time_start
        self.time = self.time_total
    
    def reset(self):
        self.time_total = 0
        self.time = 0
    
class StopWatch(Static):

    '''
     _summary_

    Yields:
        _description_
    '''

    @on(Button.Pressed, "#btn_start")
    def start_stopwatch(self):
        time_display = self.query_one(TimeDisplay)
        time_display.start()
        self.add_class("started")
    
    @on(Button.Pressed, "#btn_stop")
    def stop_stopwatch(self):
        time_display = self.query_one(TimeDisplay)
        time_display.stop()
        self.remove_class("started")

    @on(Button.Pressed, "#btn_reset")
    def reset_stopwatch(self):
        time_display = self.query_one(TimeDisplay)
        time_display.reset()

    def compose(self):
        yield Button("Start", variant="success", id="btn_start")
        yield Button("Stop", variant="error", id="btn_stop")
        yield Button("Reset", id="btn_reset")
        yield TimeDisplay()

class StopwatchApp(App):
    '''
    StopwatchApp 
    
    Base textual application class. This is the textual application entry point.

    Arguments:
        App -- Textual application base class.

    '''

    # Create application keybinds.
    # Each keybind is composed by the key, a method to invoke and a binding 
    # description.
    BINDINGS = [
        ("d", "set_dark_mode", "Dark Mode ON/OFF"),
        ("a", "add_stopwatch", "Add"),
        ("r", "remove_stopwatch", "Remove"),
        ("q", "quit_app", "Quit")
    ]

    # Define the component styling file location.
    CSS_PATH = "stopwatch.tcss"

    def compose(self):
        '''
        compose 
        
        Class method that builds the user interface with widgets.

        Yields:
            Each Yield is responsible by add an application component to the screen.
            
            Header: Show the application header at the top of the screen. You can 
            customize the header by adding components to it, like the clock
            we use in this demo.
            
            Footer: Show the application footer at the bottom of the screen and is 
            used to display any keybind we create for the application.
            
            ScrollableContainer: Define a interface container able to scroll to
            hold other application widgets.

            Stopwatch: User defined widget. Show the stopwatch interface 
            allowing the user to interact with it components.
        '''

        yield Header(show_clock=True)
        yield Footer()

        with ScrollableContainer(id="stopwatches"):
            yield StopWatch()
            yield StopWatch()
            yield StopWatch()

    def action_set_dark_mode(self):
        self.dark = not self.dark
    
    def action_add_stopwatch(self):
        new_stopwatch = StopWatch()
        self.query_one("#stopwatches").mount(new_stopwatch)
        new_stopwatch.scroll_visible()

    def action_remove_stopwatch(self):
        stopwatches = self.query("StopWatch")
        if stopwatches :
            stopwatches.last().remove()
    
    def action_quit_app(self):
        self.exit(message="Quitting Stopwatch App")

# Call the application.
if __name__ == "__main__":
    StopwatchApp().run()
    