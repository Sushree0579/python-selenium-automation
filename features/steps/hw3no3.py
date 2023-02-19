from selenium.webdriver.common.by import By
from behave import given,when,then

# @given('open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')


@when('click on cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon').click()
    #context.driver.find_element(By.CSS_SELECTOR, 'span.nav-sprite')


@then('verify that "cart_icon" is empty')
def verify_cart_icon(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h2').text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual {actual_result}'






