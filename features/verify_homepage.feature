Feature: Verify Demoblaze Homepage
  Scenario: Open Demoblaze homepage and verify title
    Given the browser is ready
    When I navigate to "https://www.demoblaze.com"
    Then the page title should be "STORE"
