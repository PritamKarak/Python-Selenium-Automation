*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome
${USERNAME}  standard_user
${PASSWORD}  secret_sauce

*** Test Cases ***
Login Using Variables
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s

    Input Text    id=user-name    ${USERNAME}
    Sleep    2s

    Input Text    id=password    ${PASSWORD}
    Sleep    2s

    Click Button    id=login-button
    Sleep    4s

    Page Should Contain    Products
    Sleep    3s

    Close Browser
