from PyQt5.QtWidgets import  QApplication
from mainUi import MainGui
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = MainGui()
    main_gui.show()
    sys.exit(app.exec())
