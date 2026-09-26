@users @crud @regression
Feature: User deletion API
  As an API automation engineer
  I want to validate user deletion
  So that delete response behavior is verified

  Background:
    Given the JSONPlaceholder User API is available

  @TC007 @positive
  Scenario: Delete a user
    When I send a DELETE request to "/users/1"
    Then the response status code should be 200
