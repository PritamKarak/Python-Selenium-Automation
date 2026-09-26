@users @crud @regression
Feature: User update APIs
  As an API automation engineer
  I want to validate full and partial user updates
  So that update contracts are verified

  Background:
    Given the JSONPlaceholder User API is available

  @TC005 @positive
  Scenario: Update a user using PUT
    Given I have a JSONPlaceholder update payload
    When I send a PUT request to "/users/1" with the update payload
    Then the response status code should be 200
    And the response should be JSON
    And the JSON field "id" should equal 1
    And the updated response should contain the submitted fields

  @TC006 @positive
  Scenario: Partially update a user using PATCH
    Given I have a JSONPlaceholder partial update payload
    When I send a PATCH request to "/users/1" with the update payload
    Then the response status code should be 200
    And the response should be JSON
    And the JSON field "id" should equal 1
    And the updated response should contain the submitted fields
