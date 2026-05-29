@echo off
cd /d "%~dp0.."
title WeMD AI - Portable Server

set "PYTHON_DIR=python"

if not exist "%PYTHON_DIR%\python.exe" (
    echo.
    echo   [FAIL] Portable Python not found!
    echo   Please run portable\setup_portable.bat first.
    echo.
    pause
    exit /b 1
)

echo.
echo   ==========================================
echo     WeMD AI - Portable Server
echo   ==========================================
echo.

if "%DEEPSEEK_API_KEY%"=="" (
    echo   [WARN] DEEPSEEK_API_KEY not set.
    echo   Run: set DEEPSEEK_API_KEY=sk-your-key
    echo.
)

echo   Starting server at http://localhost:5000
echo.

"%PYTHON_DIR%\python.exe" server.py

pause
