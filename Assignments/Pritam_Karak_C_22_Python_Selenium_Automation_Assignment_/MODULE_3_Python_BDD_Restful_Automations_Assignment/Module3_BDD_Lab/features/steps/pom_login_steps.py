from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage


@given("the login page is open")
def step_login_page(context):
    context.driver = webdriver.Chrome()
    context.page = LoginPage(context.driver)
    context.page.open()


@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.page.enter_username(username)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.page.enter_password(password)


@when("I click the login button")
def step_click_login(context):
    context.page.click_login()


@then("the user should reach the products page")
def step_success(context):
    assert "inventory" in context.driver.current_url
    context.driver.quit()


@then("a login error should be displayed")
def step_error(context):
    assert context.page.get_error_message()
    context.driver.quit()