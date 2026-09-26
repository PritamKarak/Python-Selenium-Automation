*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome

*** Test Cases ***
Verify Element Presence
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s

    Page Should Contain Element    id=user-name
    Sleep    3s

    Close Browser
