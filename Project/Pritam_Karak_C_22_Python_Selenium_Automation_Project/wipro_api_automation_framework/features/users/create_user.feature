@users @crud @regression
Feature: User creation API
  As an API automation engineer
  I want to validate user creation
  So that the API accepts valid user data

  Background:
    Given the JSONPlaceholder User API is available

  @TC004 @positive
  Scenario: Create a new user
    Given I have a JSONPlaceholder user payload
    When I send a POST request to "/users" with the user payload
    Then the response status code should be 201
    And the response should be JSON
    And the created response should contain the submitted user data
    And the created response should contain a generated id
