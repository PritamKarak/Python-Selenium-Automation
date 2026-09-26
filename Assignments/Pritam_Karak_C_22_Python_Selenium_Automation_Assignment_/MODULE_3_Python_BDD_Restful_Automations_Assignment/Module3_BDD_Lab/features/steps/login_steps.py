from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("the user opens the SauceDemo login page")
def step_open_login(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when('the user enters valid username "{username}"')
def step_username(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)


@when('the user enters valid password "{password}"')
def step_password(context, password):
    context.driver.find_element(By.ID, "password").send_keys(password)


@when("the user clicks the login button")
def step_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then("the products page should be displayed")
def step_products_page(context):
    assert "inventory" in context.driver.current_url
    assert context.driver.find_element(By.CLASS_NAME, "title").text == "Products"
    context.driver.quit()