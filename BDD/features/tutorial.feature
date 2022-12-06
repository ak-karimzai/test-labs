Feature: Create

  Scenario Outline: Create guides
     Given I put guide <firstName> <lastName> and his <experience> parameters
     When I create request
     Then I should be guide named <firstName>

    Examples:
        | firstName         | lastName            |  experience   |
        | andrey              | chalyy            |  5            |
        | andrey2             | chalyy2           |  2            |

  Scenario Outline: Create excursions
     Given I put excursion <name> <description> <guideId> <price> parameters
     When I create excursion request
     Then I should have excursion with <name> <description> <guideId> <price>
    Examples:
        | name         | description            |  guideId   | price |
        | Red_Square   | Best                   |  1         | 2000  |
        | St_Basils    | Not_the_worst          |  2         | 1500  |