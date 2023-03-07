from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

DOG_IMG = (By.CSS_SELECTOR, 'img#d')
PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, 'a[href*="privacy"]')

@given ('store original window')
def store_current_window(context):
    context.current_window = context.driver.current_window_handle
    print(context.current_window)

@when('Click on a dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handle
    print('\nAll WINDOWS: ', windows)
    context.driver.switch_to.window(windows[1])


@then('verify blog is opened')
def verify_blog_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/'))

@then('Close blog')
def close_blog(context):
    context.driver.close()

@then('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)

@given('Open Amazon T&C page')
def Amazon_TC_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_current_window(context):
    context.current_window = context.driver.current_window_handle
    print(context.current_window)

@when('Click on Amazon Privacy Notice Link')
def Privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('All WINDOWS: ', windows)
    context.driver.switch_to.window(windows[1])

@then('verify Amazon Privacy Notice Page is opened')
def verify_Amazon_Privacy_Notce_Page_opened(context):
    context.driver.wait.until(EC.url_contains)


@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.driver.switch_to.window( context.current_window)


