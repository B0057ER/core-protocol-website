# Messaging System - Deployment Guide

This is a **Node.js backend + HTML frontend** application.

⚠️ **GitHub Pages limitation:** GitHub Pages can ONLY host static files. This app requires a Node.js server, so you have two options:

## Option 1: Deploy Frontend Only to GitHub Pages

Pros: Free, fast, reliable
Cons: Messaging won't persist/share (no backend)

```bash
git remote add origin https://github.com/YOUR_USERNAME/messaging-system-frontend.git
git push -u origin main
```

Then enable GitHub Pages as you would any static site.

**Result:** Browser-only messaging (not persistent)

---

## Option 2: Deploy Full Application (Recommended)

Deploy backend + frontend together to a service that supports Node.js:

### Deploy to Vercel (Easiest)

1. **Sign up:** https://vercel.com (connect GitHub)
2. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```
3. **Deploy:**
   ```bash
   vercel
   ```
4. **Follow prompts** - your app is live!

### Deploy to Heroku

1. **Sign up:** https://heroku.com
2. **Install Heroku CLI:** https://devcenter.heroku.com/articles/heroku-cli
3. **Deploy:**
   ```bash
   heroku create your-app-name
   heroku config:set NODE_ENV=production
   git push heroku main
   ```

### Deploy to Railway.app

1. **Sign up:** https://railway.app
2. **Connect GitHub repo**
3. **Railway auto-deploys** on each push

### Deploy to Render

1. **Sign up:** https://render.com
2. **Create new Web Service**
3. **Connect GitHub**
4. **Build command:** `npm install`
5. **Start command:** `npm start`

---

## Local Development

```bash
# Install dependencies
npm install

# Start server
npm start
# or
node server.js
```

Visit `http://localhost:3000`

---

## File Structure

```
.
├── index.html          # Frontend (static)
├── server.js           # Backend (Node.js)
├── messages.json       # Data storage
├── package.json        # Dependencies
└── ...
```

---

## Recommended Setup

For best experience:
1. Deploy full app to **Vercel** or **Railway** (free tier available)
2. Frontend + backend work together seamlessly
3. Messages persist and sync across devices
4. Easy to update via git push

---

## Environment Variables

If deploying, you may need to set:
- `NODE_ENV=production`
- `PORT=3000` (usually auto-set)

Check your hosting docs for specifics.
