Feature: POM Login

  Scenario: Login successfully using Page Object Model
    Given the login page is open
    When I enter username "standard_user"
    And I enter password "secret_sauce"
    And I click the login button
    Then the user should reach the products page

  Scenario: Login with invalid credentials using Page Object Model
    Given the login page is open
    When I enter username "invalid_user"
    And I enter password "wrong_password"
    And I click the login button
    Then a login error should be displayed