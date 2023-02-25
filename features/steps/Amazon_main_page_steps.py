
from selenium.webdriver.common.by import By
from behave import given,when,then


AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
BEST_SELLERS =(By.CSS_SELECTOR,"#data-csa-c-type='link']")
#@given('open Amazon page')
def open_Amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input text {text}')
def input_search_word (context, text):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('text')

@when('Click on search button')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)
    #print(element)


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))  # '42'
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))  # => 42

    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    print(footer_links)
    print('\nLink count: ', len(footer_links))
    # assert 42 == 42
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'

#@then('Verify that text {expected_result} is shown')
def verify_search_result (context, expected_result):
        actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
        assert expected_result == actual_result, f'Expected{expected_result} but got actual {actual_result}'

@then('Verify that BestSeller has {expected_amount} links')
def verify_Best_Seller_count(context, expected_amount):
    expected_amount = int(expected_amount)
    BEST_SELLERS= context.driver.find_elements(*'BEST_SELLERS')
    assert len(BEST_SELLERS) == expected_amount, f'Expected {expected_amount} links but got {len(BEST_SELLERS)}'


@then('click on BestSeller Page')
def verify_Best_Seller_count(context):
    actual_result = context.driver.find_element(By.XPATH,"//a[contains(@href,'nav_cs_bestsellers')]").click()

@then('Verify that there are {expected_amount} links')
def verify_Best_Seeler_count(context, expected_amount):
    actual_result = context.driver.find_elements(By.CSS_SELECTOR, "#zg_header ul li")
    expected_result = 5
    assert len(actual_result) == expected_result,f'Expected {expected_result} links but got {len(actual_result)}'


