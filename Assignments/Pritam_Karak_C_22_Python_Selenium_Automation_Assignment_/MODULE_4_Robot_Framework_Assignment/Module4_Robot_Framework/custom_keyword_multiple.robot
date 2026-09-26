*** Settings ***
Library    custom_keywords.py

*** Test Cases ***
Calculate Multiple Sums
    ${result1}=    Calculate Sum    10    20
    Should Be Equal As Integers    ${result1}    30

    ${result2}=    Calculate Sum    25    15
    Should Be Equal As Integers    ${result2}    40

    ${result3}=    Calculate Sum    100    50
    Should Be Equal As Integers    ${result3}    150

    Log    All calculations completed successfully
