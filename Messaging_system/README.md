# Shared Messaging System

A simple web-based messaging system where all messages are shared across any device that accesses the website.

## Quick Start (Easiest Way)

1. **Double-click `START.bat`** in this folder
2. The server starts automatically
3. Open `http://localhost:3000` in your browser

That's it! The batch file handles everything.

## Manual Setup (If you prefer)

```bash
npm install
npm start
```

## Access from Other Devices

On a different device on the same network, go to:
```
http://<YOUR_COMPUTER_IP>:3000
```

**Find your IP address:**
- **Windows**: Open Command Prompt, type `ipconfig` (look for IPv4 like 192.168.x.x)
- **Mac/Linux**: Open Terminal, type `ifconfig`

## Features
- ✅ Messages shared instantly across all devices
- ✅ Messages persist across server restarts
- ✅ Real-time sync (updates every 2 seconds)
- ✅ Send with Enter key
- ✅ Clear all messages anytime
- ✅ Simple, clean UI

## Troubleshooting

**"Node.js is not installed"**
- Download from https://nodejs.org/
- Run START.bat again after installation

**"Can't connect from other devices"**
- Both devices must be on same WiFi
- Use correct IP address from `ipconfig`
- Keep START.bat terminal open

## Files
- `START.bat` - One-click setup & start ⭐
- `server.js` - Backend (Express)
- `index.html` - Frontend
- `package.json` - Dependencies
- `messages.json` - Auto-created message storage
