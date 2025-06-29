@echo off
REM Navigate to project root (adjust if needed)
cd /d "C:\AI\Avatar\Avatar_v1_test"

REM Activate the virtual environment
call venv310\Scripts\activate.bat

REM Run your main Python script
python main.py

REM Keep terminal open
pause
