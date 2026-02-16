# GitHub Pages Deployment Guide

## Overview
This workspace contains multiple projects. Here's how to deploy each to GitHub Pages:

## Web Projects (Can be deployed to GitHub Pages)

### 1. Core_Protocal_Website
- Static HTML/CSS site
- Ready for GitHub Pages
- **Deployment:** Push to GitHub and enable Pages in repo settings

### 2. Java_script
- Static HTML/JavaScript site  
- Ready for GitHub Pages
- **Deployment:** Push to GitHub and enable Pages in repo settings

### 3. Coolmathgames
- Static HTML site
- Ready for GitHub Pages
- **Deployment:** Push to GitHub and enable Pages in repo settings

### 4. Messaging_system
- Node.js Express server + frontend
- **Frontend only:** Can be deployed to GitHub Pages (static files)
- **Backend:** Must be deployed to a service like Heroku, Vercel, Railway, or your own server
- **Deployment:**
  1. Build/optimize static files
  2. Push to GitHub
  3. Enable GitHub Pages for the `Messaging_system` directory

## Projects (Cannot be directly deployed to GitHub Pages)

### Python Projects
- B0057TER.INC
- Recator_Core_Game  
- Stuff
- These require a Python runtime. Options:
  - Deploy to PythonAnywhere, Replit, or similar Python hosting
  - Convert to web app (Flask/Django)
  - Run locally only

### C# Project
- C sharp testing
- Requires .NET runtime
- Deploy to Azure, AWS, or similar hosting
- Cannot run on GitHub Pages

## How to Deploy to GitHub Pages

### Option 1: Single Repository with Multiple Projects
```bash
# In repository settings:
# 1. Go to Settings → Pages
# 2. Select source branch (main/master)
# 3. Select folder: / (root) to deploy from root
# 4. Save
```

### Option 2: Separate Repositories (Recommended)
Create individual repos for each web project:
```bash
git remote add origin https://github.com/YOUR_USERNAME/core-protocol-website.git
git branch -M main
git push -u origin main
```

Then enable Pages in each repository's settings.

### Option 3: GitHub Actions Deployment
Create a `.github/workflows/deploy.yml` file for automated deployment.

## Setup Checklist

- [x] `.gitignore` - Ignores unnecessary files
- [x] `.nojekyll` - Prevents Jekyll processing
- [x] HTML files - Fixed semantic HTML issues
- [ ] Set up GitHub remote repositories
- [ ] Enable GitHub Pages in repository settings
- [ ] Configure custom domain (if desired)
- [ ] Set up proper deployment branch

## Testing Locally

```bash
# Simple Python server (Python 3)
python -m http.server 8000

# Or Node.js
npx http-server
```

Then visit `http://localhost:8000`

## Common Issues

1. **Images not loading:** Ensure image paths are relative and files are committed
2. **Styling not working:** Check CSS file paths are relative, not absolute
3. **JavaScript errors:** Ensure all script includes use relative paths
4. **CORS issues:** GitHub Pages is static only, can't make server requests unless endpoint allows it

## Next Steps

1. Create GitHub repositories for each web project
2. Push code to GitHub
3. Enable GitHub Pages in repository settings
4. Test each site at `https://YOUR_USERNAME.github.io/REPO_NAME`
