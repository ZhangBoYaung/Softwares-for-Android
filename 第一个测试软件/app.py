"""
My first application
"""
import toga
from  toga.fonts import Font,SANS_SERIF
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Test(toga.App):
    main_box = toga.Box()




    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        button1 = toga.Button('点击这里！',on_press=self.fun1)
        self.main_box.add(button1)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def fun1(self,widget):
        label1 = toga.Label('运行成功！', style=Pack(padding=250))
        self.main_box.add(label1)



def main():
    return Test()

