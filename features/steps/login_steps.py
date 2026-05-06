from behave import given, when, then
from playwright.sync_api import expect
import allure

@given('que el navegador está listo')
def step_browser_ready(context):
    logout = context.page.locator("#logout2")
    if logout.is_visible():
        logout.click(timeout=10000)
        expect(context.page.locator("#login2")).to_be_visible()

@when('navego a "{url}"')
def step_navigate(context, url):
    context.page.goto(url, wait_until="domcontentloaded")

@when('hago clic en el botón de login')
def step_click_login(context):
    context.page.click("#login2", timeout=10000)
    expect(context.page.locator("#loginusername")).to_be_visible()

@when('ingreso el usuario "{username}"')
def step_enter_username(context, username):
    context.page.fill("#loginusername", username, timeout=10000)

@when('ingreso la contraseña "{password}"')
def step_enter_password(context, password):
    context.page.fill("#loginpassword", password, timeout=10000)

@when('confirmo el login')
def step_confirm_login(context):
    context.page.click('button[onclick="logIn()"]', timeout=10000)
    expect(context.page.locator("#loginModal2")).to_be_hidden()

@then('debería iniciar sesión exitosamente')
def step_verify_login(context):
    expect(context.page.locator("#logout2")).to_be_visible()
    allure.attach(context.page.url, name="url_post_login", attachment_type=allure.attachment_type.TEXT)

@then('debería ver un mensaje de error')
def step_verify_error(context):
    expect(context.page.locator("#logout2")).not_to_be_visible()
    expect(context.page.locator("#login2")).to_be_visible()
