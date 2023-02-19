rom selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='/Users/sushreechoudhary/Desktop/Automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')
#By CSS using class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-lop')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-lop')
#multiple classes=>
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-lop.icp-nav-flag-lop.icp-nav-flag')
#By CSS using attributes(except ID and class)
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
#Multiple attributes
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")
#class attributes
driver.find_element(By.CSS_SELECTOR, "a_nav-a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")
#Attributes partial match *=
driver.find_element(By.CSS_SELECTOR, "a[href *= '?ref_=nav_cs_bestsellers']")
#CSS from parent to Child
driver.find_element(By.CSS_SELECTOR,"#legalTextrow a[href*=condition_of_use]")
driver.find_element(By.CSS_SELECTOR,"div.a-section #legalTextrow a[href*=condition_of_use]")
#XPATH backwards(from child up to parent)
driver.find_element(By.XPATH, "//*[./a[contains(@href,'ap_signin_notification_condition_of_use')]]")
# Homework 3
#By CSS using classes for "amazon" and "create account"
driver.find_element(By.CSS_SELECTOR, 'i.a-icon')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
#By Css using ID for "your name" , "E-mail" ," password"
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
#By CSS using Class "password must be atleast 6 charcters"
driver.find_element(By.CSS_SELECTOR, '$$("div.a-alert-inline")')
#By CSS using ID for "Re-enter password"
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
#By Css using Class for"Create your amazon account"
driver.find_element(By.CSS_SELECTOR, 'input.a-button-input')
#By Css using attributes for "Conditions of use"
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#By Css using attributes for "Privacy Notice"
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#By Css using Class for "signin"
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')















