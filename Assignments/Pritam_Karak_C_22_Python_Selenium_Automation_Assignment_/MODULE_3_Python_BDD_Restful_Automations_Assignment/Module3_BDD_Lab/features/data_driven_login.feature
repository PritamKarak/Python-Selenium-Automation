Feature: Data Driven Login

  Scenario Outline: Login with different credentials
    Given the user opens the SauceDemo login page
    When the user enters valid username "<username>"
    And the user enters valid password "<password>"
    And the user clicks the login button
    Then the login result should be "<result>"

    Examples:
      | username        | password     | result  |
      | standard_user   | secret_sauce | success |
      | locked_out_user | secret_sauce | locked |