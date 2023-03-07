from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

@then('Verify that every product has a name and an image')
def verify_product_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(f'Amount of products found: {len(all_products)}')
    print(all_products)


    for product in all_products:
        print(product)
        assert product.find_element(*PRODUCT_IMG).is_displayed(),'product image is missing'

        product_title = product.find_element(*PRODUCT_TITLE).text
        assert product_title, 'product_title is missing'
