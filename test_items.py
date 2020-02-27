#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_basket(browser):
    browser.get(link)
#    time.sleep(30)

    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
        result = True
    except:
        result = False

    assert result == True, "Button to add product to cart not found"