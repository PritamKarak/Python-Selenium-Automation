*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome

*** Test Cases ***
Open Browser And Navigate
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    3s
    Page Should Contain    Swag Labs
    Sleep    3s
    Close Browser
