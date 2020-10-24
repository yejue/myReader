from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QBitmap, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot


class BasicPage(QWidget):
    """
    基础页面
    """

    @staticmethod
    def load_style(style: str):
        with open('./static/qss/{}'.format(style), 'r', encoding='utf8') as f:
            return f.read()

    def setShadow(self, rgb: tuple, r: int, offset=(0, 0)):
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(*offset)              # 偏移
        effect_shadow.setBlurRadius(r)                # 阴影半径
        effect_shadow.setColor(QColor(*rgb))          # 阴影颜色
        return effect_shadow


class MainPage(BasicPage):
    """
    最外层页面
    """

    @staticmethod
    def setCircle(widget):
        """
        设置成圆角
        """
        # 圆角
        bitmap = QBitmap(widget.size())
        bitmap.fill()
        painter = QPainter(bitmap)
        painter.begin(widget)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRoundedRect(bitmap.rect(), 3, 3)
        painter.end()
        widget.setMask(bitmap)

    def mousePressEvent(self, event):
        """ 无边框可移动组件1 """
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        """ 无边框可移动组件2 """
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        """ 无边框可移动组件3 """
        self.m_flag = False

    @pyqtSlot()
    def on_pushButton_close_clicked(self):
        """
        关闭窗口
        """
        self.close()

    @pyqtSlot()
    def on_pushButton_small_clicked(self):
        """
        最小化窗口
        """
        self.showMinimized()
