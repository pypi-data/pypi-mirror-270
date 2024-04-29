import os, sys
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QApplication, QWidget
import win32gui

sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from webviewpy import *

app = QApplication(sys.argv)
class _QW(QWidget):
    def resizeEvent(self, a0: QResizeEvent) -> None:  
        hwnd=self.wv.get_native_handle(webview_native_handle_kind_t.WEBVIEW_NATIVE_HANDLE_KIND_UI_WIDGET)
        win32gui.MoveWindow(hwnd, 0,100,a0.size().width(),a0.size().height()-200, True)
         
window = _QW()
window.resize(1000,500)  

wv=Webview(False,int((window.winId())))

window.wv=wv  
wv.set_title('basic') 
wv.navigate('https://www.baidu.com')
  
window.show()
sys.exit(app.exec_())