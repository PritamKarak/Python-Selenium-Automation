@authentication @regression
Feature: User authentication and account management
  As an API automation engineer
  I want to validate authentication and account lifecycle APIs
  So that valid and invalid user operations are verified

  @TC008 @positive
  Scenario: Verify login with a dynamically registered user
    Given I register a new Automation Exercise user
    When I verify login using the registered user's credentials
    Then the response status code should be 200
    And the response message should be "User exists!"
    And I delete the registered Automation Exercise user

  @TC009 @negative
  Scenario: Verify login with invalid credentials
    When I verify login using email "invalid-user@example.com" and password "WrongPassword123!"
    Then the response status code should be 200
    And the API response code should be 404
    And the response message should be "User not found!"

  @TC010 @negative
Scenario: Verify login without an email parameter
    When I verify login without an email using password "WrongPassword123!"
    Then the response status code should be 200
    And the API response code should be 400
    And the response message should be "Bad request, email or password parameter is missing in POST request."

  @TC011 @negative
Scenario: Verify login using an unsupported HTTP method
    When I send a DELETE request to "/api/verifyLogin" on the Automation Exercise API
    Then the response status code should be 200
    And the API response code should be 405
    And the response message should be "This request method is not supported."

  @TC013 @positive
  Scenario: Update a registered user's account
    Given I register a new Automation Exercise user
    When I update the registered user's account
    Then the response status code should be 200
    And the response message should be "User updated!"
    And I delete the registered Automation Exercise user

  @TC012 @positive
  Scenario: Get a registered user's account details
    Given I register a new Automation Exercise user
    When I get the Automation Exercise user details by email
    Then the response status code should be 200
    And the response should contain the registered user's email
    And I delete the registered Automation Exercise user
