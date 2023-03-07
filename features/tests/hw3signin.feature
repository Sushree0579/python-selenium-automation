# Created by sushreechoudhary at 2/17/23
Feature: Amazon Sign in page

  Scenario: Logged out users sees Sign In When Clicking on Returns and Orders
    Given Open Amazon page
    When Click on Orders and Returns page
    Then Verify that Sign in page opened

    Scenario: Sign in page can be opened from Sign in popup
      Given Open Amazon page
      When Click Sign in from popup
      Then Verify Sign in page opens

      Scenario: Sign in Popup is visible for a few seconds
        Given Open Amazon page
        Then Verify sign in popup shown
        When wait for 8 sec
        Then Verify sign in popup disappears





