# GitHub Pages site files

Place your static site files (HTML, CSS, JS, assets) inside this `docs/` folder.

How to publish:

1. Commit and push the repository to GitHub.
2. In the repository on GitHub, go to Settings → Pages.
3. Under "Build and deployment", set the source to the `main` branch (or your default branch) and the `/docs` folder.
4. Save — your site will be available at `https://<your-username>.github.io/<repo-name>/` after a short build.

Notes:
- If you already have an `index.html` in `Java_script/`, copy it into this folder along with any assets it needs.
- If you want automatic deployment from other branches, consider using a GitHub Action to push built files into `gh-pages`.
