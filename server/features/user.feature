Feature: user API
    Scenario: create user
        Given valid user
        When POST user
        Then response status code is 200
        And response contains user
        And response contains user id
