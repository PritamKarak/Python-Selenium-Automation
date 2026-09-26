*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome

*** Test Cases ***
Input Text In Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s

    Input Text    id=user-name    standard_user
    Sleep    2s

    Input Text    id=password    secret_sauce
    Sleep    3s

    Close Browser
