Feature: SauceDemo Login

  Scenario: Login with valid credentials
    Given the user opens the SauceDemo login page
    When the user enters valid username "standard_user"
    And the user enters valid password "secret_sauce"
    And the user clicks the login button
    Then the products page should be displayed