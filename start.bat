@echo off
title WeMD AI Server
echo.
echo   WeMD AI - AI Layout Engine
echo   ================================
echo.
echo   Starting server...
taskkill /f /im python.exe >nul 2>&1
echo.
start "" /b python server.py
echo   Waiting for server (3s)...
timeout /t 3 /nobreak >nul
echo   Opening browser...
start "" "http://localhost:5000"
echo.
echo   ================================
echo   Server: http://localhost:5000
echo   Press any key to stop server
echo   ================================
pause >nul
taskkill /f /im python.exe >nul 2>&1
echo   Server stopped.
