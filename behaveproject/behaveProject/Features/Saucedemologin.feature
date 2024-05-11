Feature: saucedemo Login
  Scenario:Successfull Login
    Given I am on the Demo Login Page
    When I fill the account information for account StandardUser into the Username field and the Password field
    And I click the Login Button
    Then I am redirected to the Demo Main Page
    And I verify the App Logo exists

