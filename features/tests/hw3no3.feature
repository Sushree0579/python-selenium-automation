# Created by sushreechoudhary at 2/17/23
Feature: Amazon Cart Empty
  
  Scenario: opens amazon.com, clicks on the cart icon and verifies that Your Amazon Cart is empty.
    Given Open Amazon page
      When Click on Cart icon
      Then verify that "cart_icon" is empty