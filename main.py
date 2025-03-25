import slint
import sys
import os


class MainWindow(slint.loader.ui.app_window.AppWindow):
    @slint.callback
    def request_increase_value(self):
        self.counter = self.counter + 1


main_window = MainWindow()
main_window.show()
main_window.run()
