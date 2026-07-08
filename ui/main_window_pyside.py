from PySide6.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QToolBar,
    QAction,
    QFileDialog,
    QMessageBox,
    QStatusBar,
    QMenu,
)
from PySide6.QtCore import Qt
from engine.engine import ResearchEngine
from services.excel_service import load_excel, save_excel
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CDT Healthcare Research Suite")
        self.resize(1000, 700)

        self.engine = ResearchEngine(update_callback=self._on_engine_update)

        self.df = pd.DataFrame()

        self._create_menu()
        self._create_toolbar()
        self._create_table()
        self._create_statusbar()

    def _create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        imp_action = QAction("Import Excel...", self)
        imp_action.triggered.connect(self.import_excel)
        file_menu.addAction(imp_action)

        exp_action = QAction("Export Excel...", self)
        exp_action.triggered.connect(self.export_excel)
        file_menu.addAction(exp_action)

        file_menu.addSeparator()
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        tools_menu = menubar.addMenu("Tools")
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.open_settings)
        tools_menu.addAction(settings_action)

        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)

    def _create_toolbar(self):
        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)

        import_action = QAction("Import Excel", self)
        import_action.triggered.connect(self.import_excel)
        toolbar.addAction(import_action)

        start_action = QAction("Start Research", self)
        start_action.triggered.connect(self.start_research)
        toolbar.addAction(start_action)

        pause_action = QAction("Pause", self)
        pause_action.triggered.connect(self.pause_research)
        toolbar.addAction(pause_action)

        resume_action = QAction("Resume", self)
        resume_action.triggered.connect(self.resume_research)
        toolbar.addAction(resume_action)

        export_action = QAction("Export Excel", self)
        export_action.triggered.connect(self.export_excel)
        toolbar.addAction(export_action)

    def _create_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.setAlternatingRowColors(True)
        self.setCentralWidget(self.table)

    def _create_statusbar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self._set_status("Ready")

    def _set_status(self, text: str):
        self.status.showMessage(text)

    def import_excel(self):
        path, _ = QFileDialog.getOpenFileName(self, "Import Excel", filter="Excel Files (*.xlsx *.xlsm *.xls)")
        if not path:
            return
        try:
            df = load_excel(path)
            self.df = df
            self._populate_table(df)
            self._set_status(f"Loaded {len(df)} rows from {path}")
        except Exception as e:
            QMessageBox.critical(self, "Import Error", str(e))
            self._set_status("Import failed")

    def _populate_table(self, df: pd.DataFrame):
        self.table.clear()
        cols = list(df.columns.astype(str))
        self.table.setColumnCount(len(cols))
        self.table.setHorizontalHeaderLabels(cols)
        self.table.setRowCount(len(df))

        for r_idx, row in enumerate(df.itertuples(index=False, name=None)):
            for c_idx, value in enumerate(row):
                item = QTableWidgetItem("") if pd.isna(value) else QTableWidgetItem(str(value))
                self.table.setItem(r_idx, c_idx, item)

    def export_excel(self):
        if self.df is None or self.df.empty:
            QMessageBox.information(self, "Export", "No data to export")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export Excel", filter="Excel Files (*.xlsx)")
        if not path:
            return
        try:
            save_excel(self.df, path)
            self._set_status(f"Exported {len(self.df)} rows to {path}")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", str(e))
            self._set_status("Export failed")

    def start_research(self):
        self.engine.start()
        self._set_status("Research engine started")

    def pause_research(self):
        self.engine.pause()
        self._set_status("Research engine paused")

    def resume_research(self):
        self.engine.resume()
        self._set_status("Research engine resumed")

    def open_settings(self):
        QMessageBox.information(self, "Settings", "Settings placeholder")

    def _show_about(self):
        QMessageBox.information(self, "About", "CDT Healthcare Research Suite\nPySide6 UI")

    def _on_engine_update(self, status):
        self._set_status(f"Engine: {status}")
