def test_selenium_example(driver):
    driver.get("http://localhost:8081")
    assert driver.title == "PrestaShop"
