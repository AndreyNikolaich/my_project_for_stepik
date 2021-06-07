from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/"

def test_button_add_to_basket (browser):
    browser.get(link)
    button = len(browser.find_elements(By.ID, "add_to_basket_form"))
    assert button is not None, 'Отсутствует'






