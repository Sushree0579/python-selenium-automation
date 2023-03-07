# Created by sushreechoudhary at 3/3/23
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # Enter scenario name here
    # Enter steps here
  Feature: Test for 404 page

    Scenario: user is able to navigate to amazon blog from
      Given open Amazon Product B07NFSWG011111 page
      And store original window
      When Click on a dog image
      And switch to new window
      Then verify blog is opened
      And close blog
      And return to original window

    Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original


