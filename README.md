# Portfolio website - Abdulwahab Abdulyekeen


Single page, 44 KB of HTML/CSS/JS in one file plus a 2.8 MB `assets/` folder of real screenshots.
No frameworks, no external fonts, no analytics, no tracking. Works on GitHub Pages, Netlify, Vercel,
Cloudflare Pages or any web host - it is just static files.

## Files
- `index.html` - the whole page (generated; do not hand-edit for content changes)
- `build_site.py` - the generator: copy, screenshots and project data live here
- `assets/` - desktop and mobile screenshots taken from the live apps, plus the concept mockups

## Edit then rebuild
```bash
cd portfolio-site
python3 build_site.py          # rewrites index.html
python3 -m http.server 8000    # preview at http://localhost:8000
```
Content to change is at the top of `build_site.py`: `ME` (contact details), `SERVICES`, `PROJECTS`
(problem, solution, stack, decisions, which screenshots to show) and `CONCEPTS`, `PROCESS`.
Swap a screenshot by dropping a new jpg/png into `assets/` and pointing the entry at it.

## Deploy to Vercel (fastest)
1. Push this folder to a GitHub repository (name it `portfolio`).
2. vercel.com -> Add New -> Project -> import the repo.
3. Framework preset: **Other**. Build command: *(empty)*. Output directory: `.` (or leave defaults, Vercel serves static files).
4. Deploy. Then add your own domain under Project Settings -> Domains.

Or from the terminal, no GitHub needed:
```bash
npx vercel --prod        # run inside this folder
```
Netlify works the same way: drag the folder onto app.netlify.com/drop.

## Before you publish
- Update the Fiverr "Find me on Fiverr" link in `index.html` / `build_site.py` once your gig is live
  (search for `fiverr.com`).
- Only keep claims that are true: the site says Figma and Docker - drop them from `build_site.py` if you
  do not actually use them.
- Never publish the demo numbers from the apps (47k users, 87% success, testimonials). They are sample
  content in the products, not your results.
- The three "concept designs" are labelled as AI-assisted mockups; keep that label.
