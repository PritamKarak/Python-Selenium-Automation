@users @smoke @regression
Feature: User retrieval APIs
  As an API automation engineer
  I want to validate user retrieval endpoints
  So that the user API contract is verified

  Background:
    Given the JSONPlaceholder User API is available

  @TC001 @positive
  Scenario: Get all users successfully
    When I send a GET request to "/users"
    Then the response status code should be 200
    And the response should be a JSON list
    And the response list should contain at least 1 user
    And the user list response should match the schema
    And the response time should be less than 2 seconds

  @TC002 @positive
  Scenario Outline: Get a user by valid ID
    When I send a GET request to "/users/<id>"
    Then the response status code should be 200
    And the response should be JSON
    And the JSON field "id" should equal <id>
    And the JSON field "name" should exist
    And the JSON field "email" should exist
    And the single user response should match the schema

    Examples:
      | id |
      | 1  |
      | 2  |
      | 5  |

  @TC003 @negative
  Scenario: Get a user that does not exist
    When I send a GET request to "/users/9999"
    Then the response status code should be 404
