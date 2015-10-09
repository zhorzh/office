Feature: user API
    Scenario: create user
        Given valid user
        When POST user
        Then response status code is 200
        And response contains user
        And response contains user id

    Scenario: create user twice
        Given valid user
        When POST user
        And POST user
        Then response status code is 409

    Scenario: create user without password
        Given invalid user, no password
        When POST user
        Then response status code is 400

    Scenario: create user without email
        Given invalid user, no email
        When POST user
        Then response status code is 400

    Scenario: create and read user
        Given valid user
        When POST user
        And GET user
        Then response status code is 200
        And response contains user
        And response contains user id

    Scenario: read user which is not exists
        Given user id is 0
        When GET user
        Then response status code is 404

    Scenario: create and delete user
        Given valid user
        When POST user
        And GET user
        Then response status code is 200
                        
    Scenario: create and patch user email
        Given valid user
        Given email is "xxx@gmail.com"
        When POST user
        And PATCH user email
        And GET user
        Then user email is "xxx@gmail.com"
