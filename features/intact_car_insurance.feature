Feature: Testing the intact car insurance website
    Scenario: Open the website
        Given I am on the intact car insurance website
        Then I should see the title "Quick Quote"

    Scenario: Missing form fields show error messages
        Given I am on the intact car insurance website
        When I submit the form to request an insurance quote
        Then I should see error messages for the missing fields

    Scenario: Complete the form fields to request an insurance quote new
    Given I am on the intact car insurance website
    When I fill in the following fields:
        | Field                   | Value               | Element ID                         |
        | Car Year                | 2022                | selectBox_vehicle_year_chosen      |
        | Car Make                | BMW                 | selectBox_vehicle_make_chosen      |
        | Car Model               | X7 M50i 4DR AWD     | selectBox_vehicle_model_chosen     |
        | Distance to Work/School | 10                  | kmDrivenWork                       |
        | Annual Kilometers Driven| 20,001 to 25,000 km | selectBox_vehicle_annualKm_chosen  |
        | First Name              | Vini                | firstName                          |
        | Last Name               | QA                  | lastName                           |
        | Month of Birth          | 05A                 | inputbox-dateOfBirth-month         |
        | Day of Birth            | 10                  | inputbox-dateOfBirth-day           |
        | Year of Birth           | 1984                | inputbox-dateOfBirth-year          |
        | Phone Number            | 4384351234          | phoneNumber                        |
        | Quebec Postal Code      | H3G1P1              | postalCode                         |
        | Age of Quebec Driver    | 06                  | firstLicencedAt                    |
    Then I validate the following fields:
        | Field                   | Value               | Element ID                         |
        | Car Year                | 2022                | selectBox_vehicle_year_chosen      |
        | Car Make                | BMW                 | selectBox_vehicle_make_chosen      |
        | Car Model               | X7 M50i 4DR AWD     | selectBox_vehicle_model_chosen     |
        | Distance to Work/School | 10                  | kmDrivenWork                       |
        | Annual Kilometers Driven| 20,001 to 25,000 km | selectBox_vehicle_annualKm_chosen  |
        | First Name              | Vini                | firstName                          |
        | Last Name               | QA                  | lastName                           |
        | Month of Birth          | 05                  | inputbox-dateOfBirth-month         |
        | Day of Birth            | 10                  | inputbox-dateOfBirth-day           |
        | Year of Birth           | 1984                | inputbox-dateOfBirth-year          |
        | Phone Number            | 438-435-1234        | phoneNumber                        |
        | Quebec Postal Code      | H3G1P1              | postalCode                         |
        | Age of Quebec Driver    | 06                  | firstLicencedAt                    |
    When I submit the form to request an insurance quote
    Then I should see a message asking to obtain the clients credit information
    When I submit the form to request an insurance quote
    Then I should see a loading indicator
    And I should see a message to call a representative to continue    