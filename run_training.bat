@echo off
echo ============================================================
echo Student Performance Prediction - Data Augmentation
echo ============================================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt
echo.

echo Step 2: Fetching data and training model...
python fetch_and_train.py
echo.

echo ============================================================
echo Training Complete!
echo ============================================================
echo.
echo To run the web application, execute:
echo streamlit run app.py
echo.
pause
