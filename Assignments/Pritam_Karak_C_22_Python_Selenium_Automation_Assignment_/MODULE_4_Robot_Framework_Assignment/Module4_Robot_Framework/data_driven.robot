*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=test_data.csv
Test Template    Login Test

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome

*** Test Cases ***
Login Test
    ${username}    ${password}

*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s

    Input Text    id=user-name    ${username}
    Sleep    1s

    Input Text    id=password    ${password}
    Sleep    1s

    Click Button    id=login-button
    Sleep    4s

    Page Should Contain    Products
    Sleep    3s

    Close Browser
