# Cool Math Games - Deployment Guide

This is a static HTML website ready for GitHub Pages.

## Quick Deploy to GitHub Pages

1. **Create a new repository on GitHub**
   - Name: `cool-math-games` (or your choice)
   - Make it public

2. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/cool-math-games.git
   git branch -M main
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to repo **Settings → Pages**
   - Source: `main` branch, `/ (root)` folder
   - Save

4. **Your site is live!**
   - Visit: `https://YOUR_USERNAME.github.io/cool-math-games`

## Notes

- All paths should be relative (not absolute)
- Site updates automatically when you push to GitHub
- Domain takes ~10 minutes to activate on first deploy
