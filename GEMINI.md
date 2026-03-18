# Gemini Interaction Mandates (saucedemo)

These instructions take absolute precedence over general workflows and tool defaults for all interactions within this workspace.

## 🏗️ Architectural Standards
- **Page Object Model (POM):** All UI interactions MUST be encapsulated within classes in the `pages/` directory. 
- **Assertions in Pages:** Page classes should include assertion methods (e.g., `assert_loaded`, `assert_product_title`) to keep test files clean and focused on flow.
- **Locators:** Use Playwright's recommended locators (e.g., `get_by_role`, `get_by_text`, `get_by_test_id`) over CSS/XPath where possible.
- **Allure Integration:** Every action method in a Page class MUST be wrapped in an `@allure.step` decorator.

## 🐍 Python & Tooling
- **Dependency Management:** Use `uv` exclusively for package management and running commands (e.g., `uv run pytest`).
- **Sync API:** This project uses the Playwright **Synchronous** API. Do not use `async/await`.
- **Typing:** Use type hints for all method signatures and class attributes.

## 🧪 Testing & Validation
- **Reporting:** Always run tests with `--alluredir=artifacts/allure-results` to ensure reports are generated.
- **Failures:** On test failure, ensure screenshots and traces are captured in the `artifacts/` directory (managed via `conftest.py`).
- **Clean State:** Tests should be independent; ensure the browser context is properly managed between tests.

## 📝 Style Guidelines
- **Naming:** 
  - Page Classes: `PascalCase` (e.g., `LoginPage`)
  - Test Files: `test_*.py`
  - Methods/Variables: `snake_case`
- **Documentation:** Maintain the professional and concise style established in the existing codebase.
