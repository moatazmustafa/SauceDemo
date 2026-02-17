<!-- =========================================================
  SauceDemo – Playwright Framework README
========================================================== -->

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=700&center=true&vCenter=true&width=980&lines=%F0%9F%94%A5+SauceDemo+UI+Automation+Framework;%E2%9A%A1+Playwright+%2B+Pytest+%2B+POM+%2B+Allure;%F0%9F%9A%80+Traces+%2B+Screenshots+on+Failure+%7C+Logging+%7C+CI" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-00D1FF?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Playwright-Sync-39FF14?style=for-the-badge&logo=playwright&logoColor=black" />
  <img src="https://img.shields.io/badge/Pytest-Runner-FF2BD6?style=for-the-badge&logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/Allure-Reports-FFD300?style=for-the-badge&logo=allure&logoColor=black" />
  <img src="https://img.shields.io/badge/GitHub_Actions-CI-7A5CFF?style=for-the-badge&logo=githubactions&logoColor=white" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00D1FF,50:FF2BD6,100:39FF14&height=120&section=header&text=SauceDemo%20Automation&fontSize=36&fontColor=0b0f1a&animation=twinkling" />
</p>

---

# 🧪 SauceDemo – Playwright Framework UI Automation

> A clean, scalable UI automation framework built for real-world testing:
**Playwright (Python sync)** + **Pytest** + **POM** + **Allure**  
with **trace/screenshot on failure**, **logging**, and **CI**.

---

## ⚡ Quick Start (3 commands)

```bash
uv sync
uv run playwright install --with-deps
PW_HEADLESS=0 uv run pytest -q

## ✨ What is this?
A **clean, scalable UI automation framework** built with:

✅ Playwright (Python sync)  
✅ Pytest  
✅ Page Object Model (POM)  
✅ Allure reporting (steps + attachments)  
✅ Auto **trace + screenshot** on failure  
✅ Real logging (**console + file**)  
✅ Ready for GitHub Actions CI  

---

## 🗂️ Project Structure

```text
odoo-qa/
├─ pages/                 # POM: locators + actions + assertions (+ Allure steps)
├─ tests/                 # Test cases (E2E / smoke / regression)
├─ utils/                 # Helpers (logger, shared utilities)
├─ artifacts/             # Generated outputs (usually ignored in git)
│  ├─ allure-results/
│  ├─ allure-report/
│  ├─ traces/
│  ├─ screenshots/
│  └─ logs/
├─ conftest.py            # Fixtures: browser/page lifecycle + failure attachments
├─ pytest.ini             # Pytest settings (logging, markers, etc.)
├─ pyproject.toml         # Dependencies / project config
└─ README.md

⸻

⚙️ Setup
uv sync
2) Install Playwright browsers
uv run playwright install --with-deps

⸻

▶️ Run Tests
👁️ Headed (show browser)
PW_HEADLESS=0 uv run pytest -q
🤖 Headless (CI mode)
PW_HEADLESS=1 uv run pytest -q

⸻

📊 Allure Report (Full Workflow)
Run tests → generate report → open report
rm -rf artifacts/allure-results artifacts/allure-report
PW_HEADLESS=0 uv run pytest -q --alluredir=artifacts/allure-results
allure generate artifacts/allure-results -o artifacts/allure-report --clean
allure open artifacts/allure-report
✅ On failure, Allure will include:
	•	Screenshot (PNG)
	•	Playwright trace (ZIP) you can open with:
🧩 Open a Playwright trace
(From Allure attachment OR from artifacts folder)
uv run playwright show-trace artifacts/traces/<trace-file>.zip

⸻

🧾 Logging

Outputs:
	•	artifacts/logs/run.log (framework log)
	•	artifacts/logs/pytest.log (pytest logging)

If you don’t see logs in terminal, run with:
uv run pytest -s

⸻

🧠 Page Object Model Rules (Best Practice)

Pages should contain:
	•	locators
	•	actions (click/fill/navigation)
	•	assertions (assert_loaded, assert_totals…)
	•	with allure.step("..."): inside methods

Tests should:
	•	be clean and readable
	•	call Page methods only
	•	avoid direct locators unless absolutely necessary
🧪 Example Test Flow (E2E Checkout)

✔ Login
✔ Assert home loaded + title
✔ Open product #1 → assert title → add → back
✔ Open product #2 → assert title → add → back
✔ Open cart → assert items
✔ Checkout info → fill & continue
✔ Overview totals → assert
✔ Finish → assert success message

⸻

✅ Recommended .gitignore

Put this in your .gitignore file
# artifacts
artifacts/allure-results/
artifacts/allure-report/
artifacts/traces/
artifacts/screenshots/
artifacts/logs/

# python
.venv/
__pycache__/
*.pyc

⸻

🤖 GitHub Actions CI (Ready)

Create this file:
.github/workflows/tests.yml
name: UI Tests (Playwright + Pytest)

on:
  push:
    branches: [ "master", "main" ]
  pull_request:
    branches: [ "master", "main" ]

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install uv
        run: pip install uv

      - name: Install dependencies
        run: uv sync

      - name: Install Playwright browsers
        run: uv run playwright install --with-deps

      - name: Run tests (headless) + Allure results
        run: |
          PW_HEADLESS=1 uv run pytest -q --alluredir=artifacts/allure-results

      - name: Upload Allure results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: allure-results
          path: artifacts/allure-results

⸻

🚀 Push to GitHub (Quick Commands)
git status
git add .
git commit -m "Add POM pages, Allure, logging, CI, and docs"
git remote -v
git push -u origin master

⸻

👤 Author

Moataz Mustafa
LinkedIn
Email: moatazmustafa123@gmail.com