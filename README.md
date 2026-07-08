# CDT-Healthcare-Research-Suite

Windows Setup and Run Instructions

1. Clone the repository:

```powershell
git clone https://github.com/KSea613/CDT-Healthcare-Research-Suite.git
cd CDT-Healthcare-Research-Suite
```

2. Create and activate a Python virtual environment (Windows PowerShell example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the application:

```powershell
python run.py
```

Notes:
- This project uses PySide6 for the GUI on Windows. Do not attempt to open the GUI inside Codespaces; run the app on a local Windows machine with a graphical session.
- Excel import/export uses `pandas` and `openpyxl`.
- If you encounter missing dependencies, run `pip install PySide6 pandas openpyxl`.

Importing an Ontario Ministry LTC Excel

1. Start the application (`python run.py`).
2. Use the toolbar button labeled "Import Ministry LTC Excel" or select "File -> Import Excel...".
3. In the file dialog select the `.xlsx` file exported from the Ontario Ministry LTC dataset.
4. The app reads the first worksheet using `openpyxl` and displays it in the central table.
5. The status bar shows the number of imported rows.

Error handling:
- If the selected file is not a valid Excel workbook, the app will show an error dialog and the status bar will report the failure.
