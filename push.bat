@echo off
chcp 65001 >nul
title Git Push - WeMD AI
cd /d "%~dp0.."

echo.
echo   ==========================================
echo     WeMD AI - Git Push
echo   ==========================================
echo.

set RETRIES=0
set MAX_RETRIES=20

:push
set /a RETRIES+=1
echo   [%RETRIES%/%MAX_RETRIES%] Pushing to GitHub...

git push
if %errorlevel% equ 0 (
    echo.
    echo   ==========================================
    echo     Push successful!
    echo   ==========================================
    goto :end
)

echo   [FAIL] Push failed (attempt %RETRIES%/%MAX_RETRIES%)
if %RETRIES% geq %MAX_RETRIES% (
    echo.
    echo   [ABORT] Max retries reached.
    echo   Try again later or check your connection.
    goto :end
)

echo   Retrying in 5 seconds...
timeout /t 5 /nobreak >nul
goto :push

:end
echo.
pause
