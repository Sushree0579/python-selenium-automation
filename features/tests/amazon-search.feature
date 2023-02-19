# Created by sushreechoudhary at 2/15/23
Feature: Amazon search tests
  Scenario: user can search for a coffee on Amazon
    Given open Amazon page
    When Input text coffee
    When Click on search button
    Then Verify the text "coffee" is shown


    Scenario: user can search for a table on Amazon
    Given open Amazon page
    When Input text table
    When Click on search button
    Then Verify the text "table" is shown


