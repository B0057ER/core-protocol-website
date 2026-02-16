# Core Protocol Website - Deployment Guide

This is a static HTML website ready for GitHub Pages.

## Quick Deploy to GitHub Pages

1. **Create a new repository on GitHub**
   - Name: `core-protocol-website` (or your choice)
   - Make it public

2. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/core-protocol-website.git
   git branch -M main
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to repo **Settings → Pages**
   - Source: `main` branch, `/ (root)` folder
   - Save

4. **Your site is live!**
   - Visit: `https://YOUR_USERNAME.github.io/core-protocol-website`

## Assets Needed

Make sure these files exist in the directory:
- ✅ `CG1.png`
- ✅ `CG2.png`
- ✅ `CG3.png`
- ✅ `pengue.jpg` (optional)

## Notes

- All paths are relative (no absolute paths)
- Site updates automatically when you push to GitHub
- Domain takes ~10 minutes to activate on first deploy
