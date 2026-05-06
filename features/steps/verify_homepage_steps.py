from behave import given, when, then

@given('the browser is ready')
def step_browser_ready(context):
    pass

@when('I navigate to "{url}"')
def step_navigate(context, url):
    context.page.goto(url, timeout=60000, wait_until="domcontentloaded")

@then('the page title should be "{title}"')
def step_verify_title(context, title):
    actual_title = context.page.title()
    assert actual_title == title, f"Expected: '{title}', got: '{actual_title}'"
