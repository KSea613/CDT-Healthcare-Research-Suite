import sys
from ui.main_window_pyside import MainWindow


def run_app():
    # Import Qt application inside the runner so importing this module
    # doesn't require Qt system libraries (useful for CI or Codespaces).
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
