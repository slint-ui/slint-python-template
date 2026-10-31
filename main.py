import slint


class MainWindow(slint.loader.slint_project.AppWindow):
    @slint.callback
    def request_increase_value(self):
        self.counter = self.counter + 1


main_window = MainWindow()
main_window.show()
main_window.run()
