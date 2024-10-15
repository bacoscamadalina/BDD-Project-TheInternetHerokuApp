from driver import Driver
from pages.base_page import BasePage


def before_all(context):
    context.driver = Driver()
    context.base_page = BasePage()

def after_all(context):
    context.driver.close()

