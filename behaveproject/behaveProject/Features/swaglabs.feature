Feature: swaglabs product checkout
Scenario: 3 Order a product
   Given I am on the inventory page
   When user sorts products from high price to low price
   And user adds highest priced product
   And user clicks on cart
   And user clicks on checkout
   And user enters first name Alice
   And user enters last name Doe
   And user enters zip code 592
   And user clicks Continue button
   Then I verify in Checkout overview page if the total amount for the added item is $49.99
   When user clicks Finish button
   Then Thank You header is shown in Checkout Complete page