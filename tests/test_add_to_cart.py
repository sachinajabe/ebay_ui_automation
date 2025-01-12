def test_login(driver):
    from pages.add_to_cart import AddToCart

    add_to_cart_page = AddToCart(driver)
    driver.get("https://www.ebay.com/")
    add_to_cart_page.add_to_cart()
    assert "1" in "1"
