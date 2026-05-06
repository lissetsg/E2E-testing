from behave import given, when, then

@given('que el navegador está listo')
def step_browser_ready(context):
    if context.page.is_visible('#logout2', timeout=3000):
        context.page.click('#logout2', timeout=10000)
        context.page.wait_for_selector('#login2', timeout=10000)

@when('navego a "{url}"')
def step_navigate(context, url):
    context.page.goto(url, timeout=60000, wait_until="domcontentloaded")

@when('hago clic en el botón de login')
def step_click_login(context):
    context.page.click('#login2', timeout=10000)
    context.page.wait_for_selector('#loginusername', timeout=10000)

@when('ingreso el usuario "{username}"')
def step_enter_username(context, username):
    context.page.fill('#loginusername', username, timeout=10000)

@when('ingreso la contraseña "{password}"')
def step_enter_password(context, password):
    context.page.fill('#loginpassword', password, timeout=10000)

@when('confirmo el login')
def step_confirm_login(context):
    context.page.click('button[onclick="logIn()"]', timeout=10000)
    context.page.wait_for_selector('#loginModal2', timeout=10000, state='hidden')

@then('debería iniciar sesión exitosamente')
def step_verify_login(context):
    context.page.wait_for_selector('#logout2', timeout=10000)
    logout_visible = context.page.is_visible('#logout2', timeout=10000)
    assert logout_visible, "Expected logout button to be visible after login"

@then('debería ver un mensaje de error')
def step_verify_error(context):
    context.page.wait_for_selector('#login2', timeout=10000)
    logout_exists = context.page.is_visible('#logout2', timeout=3000)
    assert not logout_exists, "Expected logout button to NOT be visible (login should have failed)"
