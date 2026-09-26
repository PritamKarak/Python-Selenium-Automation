*** Settings ***
Library    custom_keywords.py

*** Test Cases ***
Calculate Sum Using Custom Keyword
    ${result}=    Calculate Sum    10    20
    Log    The calculated sum is ${result}
    Should Be Equal As Integers    ${result}    30
