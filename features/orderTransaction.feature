Feature: Order Transaction
  Tests related to Order Transaction

  Scenario Outline: Verify Order success message shown in details page
    Given place the item order with <username> and <password>
    And user is on landing page
    When I login to portal with <username> and <password>
    And navigate to orders page
    Then select the orderId & verify order message is successfully delivered
    Examples:
      | username                          | password |
      | azharulla.mohammed1701@gmail.com  | 1234567  |
      | ajju.jas@gmail.com                | 1234567  |