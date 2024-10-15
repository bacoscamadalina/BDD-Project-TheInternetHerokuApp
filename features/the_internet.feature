Feature: Test the login functionality of the internet heroku app
  # https://the-internet.herokuapp.com/login
  Background:
    Given I am on the login page
  Scenario: Check valid credentials
    When I enter a valid username
    And I enter a valid password
    When I click on login button
    Then I am on the secured area
    And I am on a new page
    #https://the-internet.herokuapp.com/secure
  @invalidLogin
  Scenario Outline: Test invalid credentials
    When I use invalid "<username>" or "<password>"
    And I click on login button
    Then I should remain on the login page
    Examples:
      | username | password |
      | username | password |
      | tomsmith | password |
      | username | SuperSecretPassword! |