@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0.."
title WeMD AI - Portable Setup

set "PYTHON_VERSION=3.10.11"
set "PYTHON_DIR=python"
set "PYTHON_ZIP=python-%PYTHON_VERSION%-embed-amd64.zip"
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_ZIP%"
set "GET_PIP_URL=https://bootstrap.pypa.io/get-pip.py"
set "PIP_TRUSTED=--trusted-host pypi.org --trusted-host files.pythonhosted.org"
set "PIP_INDEX=https://pypi.org/simple/"

echo.
echo   ==========================================
echo     WeMD AI - Portable Python Setup
echo   ==========================================
echo.
echo   This will download embedded Python 3.10
echo   and install required packages locally.
echo   Total size: ~45 MB. One-time setup only.
echo.

:: Check if already installed
if exist "%PYTHON_DIR%\python.exe" (
    echo   [*] Found existing python\ directory.
    choice /c YN /t 10 /d N /m "  Reinstall? (Y/N)" >nul
    if errorlevel 2 (
        echo   [!] Skipping setup, verifying...
        goto :verify
    )
    echo   Removing old python\ ...
    rmdir /s /q "%PYTHON_DIR%" 2>nul
)

:: Download Python embeddable
echo.
echo   [1/4] Downloading Python %PYTHON_VERSION% ...
if exist "%PYTHON_ZIP%" del /f /q "%PYTHON_ZIP%"
curl -s -o "%PYTHON_ZIP%" "%PYTHON_URL%" 2>nul
if not exist "%PYTHON_ZIP%" (
    powershell -Command "$ProgressPreference='SilentlyContinue'; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_ZIP%';" 2>nul
)
if not exist "%PYTHON_ZIP%" (
    echo   [FAIL] Download failed! Check internet or use a VPN.
    pause
    exit /b 1
)
echo   [OK] Downloaded

:: Extract
echo.
echo   [2/4] Extracting to %PYTHON_DIR%\ ...
if not exist "%PYTHON_DIR%" mkdir "%PYTHON_DIR%"
powershell -Command "Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath '%PYTHON_DIR%' -Force;" 2>nul
if not exist "%PYTHON_DIR%\python.exe" (
    tar -xf "%PYTHON_ZIP%" -C "%PYTHON_DIR%" 2>nul
)
if not exist "%PYTHON_DIR%\python.exe" (
    echo   [FAIL] Extraction failed!
    pause
    exit /b 1
)
del /f /q "%PYTHON_ZIP%"
echo   [OK] Extracted

:: Enable site-packages
echo.
echo   [3/4] Configuring embedded Python ...
for %%f in ("%PYTHON_DIR%\python*._pth") do (
    powershell -Command "$c = Get-Content '%%f' -Raw; $c = $c -replace '#import site', 'import site'; $c = $c -replace '# Lib\\site-packages', 'Lib\\site-packages'; Set-Content -Path '%%f' -Value $c -NoNewline;" 2>nul
)
if not exist "%PYTHON_DIR%\Lib\site-packages" mkdir "%PYTHON_DIR%\Lib\site-packages"
echo   [OK] Configured

:: Install pip via get-pip.py
echo.
echo   [4/4] Installing pip and project dependencies ...
curl -s -o "%PYTHON_DIR%\get-pip.py" "%GET_PIP_URL%" 2>nul
if not exist "%PYTHON_DIR%\get-pip.py" (
    powershell -Command "Invoke-WebRequest -Uri '%GET_PIP_URL%' -OutFile '%PYTHON_DIR%\get-pip.py';" 2>nul
)

:: Install pip (with trusted-host to handle embedded Python SSL quirks)
echo        Installing pip...
"%PYTHON_DIR%\python.exe" "%PYTHON_DIR%\get-pip.py" --no-warn-script-location %PIP_TRUSTED% -i %PIP_INDEX% >nul 2>&1
if %errorlevel% neq 0 (
    echo   [FAIL] pip installation failed!
    echo        Try running this script again or check your internet.
    pause
    exit /b 1
)
del /f /q "%PYTHON_DIR%\get-pip.py"

:: Install project deps
echo        Installing flask + requests...
"%PYTHON_DIR%\Scripts\pip.exe" install --no-warn-script-location %PIP_TRUSTED% -i %PIP_INDEX% flask requests >nul 2>&1
if %errorlevel% neq 0 (
    echo   [FAIL] Package installation failed!
    pause
    exit /b 1
)
echo   [OK] Dependencies installed

:: Verify
:verify
echo.
echo   --- Environment Check ---
"%PYTHON_DIR%\python.exe" -c "import flask, requests, sys; print('  Python', sys.version.split()[0]); print('  Flask', flask.__version__); print('  requests', requests.__version__)"
if %errorlevel% neq 0 (
    echo   [FAIL] Verification failed! Try running this script again.
    pause
    exit /b 1
)

echo.
echo   ==========================================
echo     Setup complete!
echo   ==========================================
echo.
echo   To start the server:
echo     portable\start_portable.bat
echo.
echo   Set your DeepSeek API key first:
echo     set DEEPSEEK_API_KEY=sk-your-key
echo     portable\start_portable.bat
echo.
pause
