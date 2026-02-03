from playwright.sync_api import expect


def test_login_only(page):
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.locator("[data-test='inventory-item-name']", has_text= "Sauce Labs Backpack").click()
    page.locator("[data-test='add-to-cart']", has_text= "Add to cart").click()
    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='checkout']", has_text= "Checkout").click()
    page.get_by_placeholder("First Name").fill("Moataz Mustafa")
    page.get_by_placeholder("Last Name").fill("Hammam")
    page.get_by_placeholder("Zip/Postal Code").fill("57653")
    page.locator("[data-test='continue']", has_text= "continue").click()
    total = page.locator("[data-test='total-label']")
    expect(total).to_have_text("Total: $32.39")
    page.locator("[data-test='finish']", has_text= "Finish").click()
    expect(page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")

    # page.locator("[data-test='']", has_text= "").click()
    # page.locator("[data-test='']", has_text= "").click()
    # page.locator("[data-test='']", has_text= "").click()
    # page.locator("[data-test='']", has_text= "").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
