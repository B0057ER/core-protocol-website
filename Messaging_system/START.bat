@echo off
setlocal enabledelayedexpansion

REM Change to the script's directory
cd /d "%~dp0"

echo.
echo ======================================
echo  Simple Messaging System
echo ======================================
echo.

REM Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed!
    echo Please install Node.js from https://nodejs.org/
    echo Then RESTART YOUR COMPUTER before running this script again
    echo.
    pause
    exit /b 1
)

echo Node.js found!
node --version
echo.

REM Check if npm modules are installed
if not exist "node_modules\" (
    echo Installing dependencies (first time only)...
    call npm install
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo Dependencies installed!
    echo.
) else (
    echo Dependencies already installed.
    echo.
)

echo Starting server...
echo.
echo ======================================
echo Server running on: http://localhost:3000
echo ======================================
echo.
echo Open this link: http://localhost:3000
echo.
echo To access from iPad/other devices:
echo 1. Open Command Prompt
echo 2. Type: ipconfig
echo 3. Find IPv4 address (like 192.168.x.x)
echo 4. On iPad use: http://YOUR_IP:3000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the server
call npm start

REM If npm start fails, show error
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Server failed to start!
    echo.
)

pause
