import slint
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "ui"))

class MainWindow(slint.loader.app_window.AppWindow):
    @slint.callback
    def request_increase_value(self):
        self.counter = self.counter + 1

main_window = MainWindow()
main_window.show()
main_window.run()