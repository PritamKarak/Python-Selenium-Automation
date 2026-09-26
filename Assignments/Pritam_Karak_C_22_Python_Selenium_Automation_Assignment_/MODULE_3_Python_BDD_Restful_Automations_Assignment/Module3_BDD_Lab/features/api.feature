Feature: API Testing

  Scenario: Verify API response
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts/1"
    When I send a GET request
    Then the response status code should be 200
    And the response ID should be 1