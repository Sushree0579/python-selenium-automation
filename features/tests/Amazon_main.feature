# Created by sushreechoudhary at 2/21/23
Feature: Amazon main page tests

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon present

  Scenario: Footer and header has correct amount of links
    Given Open amazon page
    Then Verify that footer has 42 links
    Then Verify that header has 29 links


   Scenario: User can see 5 links on Amazon BesSellers Page
     Given Open amazon page
     Then click on BestSeller Page
     Then Verify that there are 5 links