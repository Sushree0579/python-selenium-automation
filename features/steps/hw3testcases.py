from selenium.webdriver.common.by import By
from behave import given,when,then


@given('open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Orders and Returns page')
def orders_returns(context):
    context.driver.find_element(By.ID, 'nav-orders').click()
   # context.driver.find_element(By.CSS_SELECTOR, 'span.nav-line-2').click()


@then('Verify that Sign in page opened')
def verify_sign_in(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual {actual_result}'





