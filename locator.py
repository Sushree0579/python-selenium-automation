from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='/Users/sushreechoudhary/Desktop/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

#Homework Amazon logo by xpath
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
#Continue Button
driver.find_element(By.ID, 'continue')
#Need help?
driver.find_element(By.XPATH, "//span[contains(text(), 'Need help')]")

#Forgot your password link
driver.find_element(By.XPATH,"//a[@class='a-link-normal']")
#Other issue with sign-in
driver.find_element(By.ID,'ap-other-signin-issues-link')
#create your Amazon Account Button
driver.find_element(By.ID,'createAccountSubmit')
#Condition of use link
driver.find_element(By.XPATH,"//a[@rel='noopener']")
#Privacy Notice link
driver.find_element(By.XPATH,"//a[@rel='noopener']")
#homework no.2 Create a test case for the Sign In page using python & selenium script
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'nav-orders')
driver.find_element(By.ID, 'nav-orders').click()
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//h1[@class='a--spacing-small']").text
print(actual_result)
assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')






