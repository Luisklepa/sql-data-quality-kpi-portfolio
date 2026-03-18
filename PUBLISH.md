# Publish to GitHub

This repo is ready for public publication. Git is initialized and the initial commit is done.

## Pre-publish checklist (completed)

- [x] No secrets, tokens, or credentials in the repo
- [x] `.gitignore` excludes: `.env`, `output/`, `*.db`, `venv/`, `__pycache__`, `jd.txt`; allows `_shared/data/*.csv` and `02-data-quality-kpi-pack/data/dirty/*.csv`
- [x] README is the final public version (sober, no heavy personal details)
- [x] Repo name for GitHub: **sql-data-quality-kpi-portfolio**
- [x] Content is safe and appropriate for a public portfolio

## What you need to do

1. **Create the repository on GitHub**
   - Go to [github.com/new](https://github.com/new)
   - **Repository name:** `sql-data-quality-kpi-portfolio`
   - **Visibility:** Public
   - Do **not** add a README, .gitignore, or license (this repo already has them)
   - Click **Create repository**

2. **Set the remote URL** (replace `YOUR_GITHUB_USERNAME` with your GitHub username)

   A placeholder remote may already be set. Update it:

   ```bash
   cd "c:\Users\User\Desktop\LIMITLESS"
   git remote set-url origin https://github.com/YOUR_GITHUB_USERNAME/sql-data-quality-kpi-portfolio.git
   ```

   If you have not added a remote yet:

   ```bash
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/sql-data-quality-kpi-portfolio.git
   ```

3. **Push** (use `main` or `master` depending on your default branch)

   ```bash
   git branch -M main
   git push -u origin main
   ```

   Or, if you keep `master`:

   ```bash
   git push -u origin master
   ```

4. **Set the repo description and topics on GitHub**
   - **Description:** Portfolio: SQL, KPI reporting, data quality, dimensional modeling. Technical Data Analyst / BI Analyst.
   - **Topics:** `sql` `power-bi` `data-analytics` `kpi` `data-quality` `reporting` `business-intelligence` `portfolio`

## Final repo URL (after you create and push)

`https://github.com/YOUR_GITHUB_USERNAME/sql-data-quality-kpi-portfolio`

---

*You can delete this file after publishing if you prefer; it is for one-time setup only.*
