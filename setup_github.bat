@echo off
echo ========================================
echo   Student Performance Prediction
echo   GitHub Setup Script
echo ========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo.
    echo Please download and install Git from:
    echo https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo Git is installed. Proceeding...
echo.

REM Get GitHub username
set /p GITHUB_USERNAME="Enter your GitHub username: "
echo.

REM Initialize Git repository
echo [1/5] Initializing Git repository...
git init
if errorlevel 1 (
    echo ERROR: Failed to initialize Git repository
    pause
    exit /b 1
)
echo Done!
echo.

REM Add all files
echo [2/5] Adding all files...
git add .
if errorlevel 1 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)
echo Done!
echo.

REM Commit files
echo [3/5] Committing files...
git commit -m "Initial commit - Student Performance Prediction System"
if errorlevel 1 (
    echo ERROR: Failed to commit files
    pause
    exit /b 1
)
echo Done!
echo.

REM Set main branch
echo [4/5] Setting main branch...
git branch -M main
echo Done!
echo.

REM Add remote repository
echo [5/5] Adding remote repository...
git remote add origin https://github.com/%GITHUB_USERNAME%/student-performance-prediction.git
if errorlevel 1 (
    echo WARNING: Remote might already exist or invalid username
    echo You can manually add it later with:
    echo git remote add origin https://github.com/%GITHUB_USERNAME%/student-performance-prediction.git
)
echo Done!
echo.

echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Next steps:
echo.
echo 1. Create a repository on GitHub:
echo    - Go to: https://github.com/new
echo    - Name: student-performance-prediction
echo    - Make it PUBLIC
echo    - Don't initialize with README
echo    - Click "Create repository"
echo.
echo 2. Push your code:
echo    git push -u origin main
echo.
echo 3. Deploy on Streamlit Cloud:
echo    - Go to: https://streamlit.io/cloud
echo    - Sign in with GitHub
echo    - Click "New app"
echo    - Select your repository
echo    - Set main file: app.py
echo    - Click "Deploy"
echo.
echo Your app will be live in 2-3 minutes!
echo.
pause
