from pywinauto import Application as WinApplication


class Application:

    def __init__(self, target):
        self.application = WinApplication(backend="win32").start(target)
        self.main_window = self.application.window(title="Free Address Book")
        self.main_window.wait("visible")
        #self.application = WinApplication(backend="uia").start(target)



    def destroy(self):
        self.main_window .close()