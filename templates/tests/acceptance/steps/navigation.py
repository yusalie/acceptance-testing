from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome('/Users/Yusuf Salie/Downloads/chromedriver_win32 (1)/chromedriver')
    browser.get('http://127.0.0.1:5000')