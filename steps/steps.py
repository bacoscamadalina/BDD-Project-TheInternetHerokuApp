from behave import given, when, then


@given(u'I am on the login page')
def step_impl(context):
    context.base_page.navigate_to_login()
    print(u'STEP: Given I am on the login page')


@when(u'I enter a valid username')
def step_impl(context):
    context.base_page.enter_username()
    (u'STEP: When I enter a valid username')


@when(u'I enter a valid password')
def step_impl(context):
    context.base_page.enter_password()
    print(u'STEP: When I enter a valid password')


@when(u'I click on login button')
def step_impl(context):
    context.base_page.click_login_button()
    print(u'STEP: When I click on login button')


@then(u'I am on the secured area')
def step_impl(context):
    context.base_page.validate_secure()
    print(u'STEP: Then I am on the secured area')


@then(u'I am on a new page')
def step_impl(context):
    context.base_page.validate_url()
    print(u'STEP: Then I am on a new page')

@when(u'I use invalid "{username}" or "{password}"')
def step_impl(context,username,password):
    context.base_page.enter_invalid(username,password)


@then(u'I should remain on the login page')
def step_impl(context):
    context.base_page.validate_sameURL()
    print(u'STEP: Then I should remain on the login page')


