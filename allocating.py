import sys
from PyQt5.QtWidgets import QApplication


from main_controller import MainController


class AllocatingCenter(MainController):
    """
    分拨中心
    """
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainController()
    win.show()
    sys.exit(app.exec_())
