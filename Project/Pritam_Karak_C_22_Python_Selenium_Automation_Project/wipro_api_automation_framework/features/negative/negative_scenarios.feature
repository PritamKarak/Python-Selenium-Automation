@negative @regression
Feature: Negative API testing
  As an API automation engineer
  I want to validate error handling
  So that invalid requests are handled as expected

  @TC013 @negative
  Scenario: Unsupported POST method for products list
    When I send a POST request to "/api/productsList" on the Automation Exercise API
    Then the response status code should be 405

  @TC014 @negative
  Scenario: Search product without required parameter
    When I send a POST request to "/api/searchProduct" on the Automation Exercise API without a search_product parameter
    Then the response status code should be 400
    And the response message should be "Bad request, search_product parameter is missing in POST request."

  @TC015 @negative
  Scenario: Unsupported PUT method for brands list
    When I send a PUT request to "/api/brandsList" on the Automation Exercise API
    Then the response status code should be 405
