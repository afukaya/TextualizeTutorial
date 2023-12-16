from time import monotonic
from textual import on
from textual.app import App
from textual.widgets import Header, Footer, Static, Button
from textual.reactive import reactive
from textual.containers import ScrollableContainer

class TimeDisplay(Static):
    
    time_enlapsed = reactive(0)
    time_start    = monotonic()
    time_total    = 0

    def on_mount(self):
        self.update_timer = self.set_interval(1/60,self.update_time_enlapsed(),pause=True)

    def update_time_enlapsed(self):
        self.time_enlapsed = self.time_total + (monotonic() - self.time_start)

    def watch_time_enlapsed(self):
        time = self.time_enlapsed
        minutes, seconds = divmod(time,60)
        hours, minutes = divmod(minutes,60)
        self.update = (f"{hours:02,.0f}:{minutes:02,.0f}:{seconds:05.2f}")

    def start(self):
        self.start_time = monotonic()
        self.update_timer.resume()
    
    def stop(self):
        self.update_timer.pause()
        self.time_total += monotonic() - self.start_time
        self.time = self.time_total
    
    def reset(self):
        self.time_total = 0
        self.time = 0
    
class StopWatch(Static):

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

    BINDINGS = [
        ("d", "set_dark_mode", "Dark Mode ON/OFF")
    ]

    CSS_PATH = "stopwatch.css"

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

        with ScrollableContainer(id="stopwatches"):
            yield StopWatch()
            yield StopWatch()
            yield StopWatch()

    def action_set_dark_mode(self):
        self.dark = not self.dark

if __name__ == "__main__":
    StopwatchApp().run()
    