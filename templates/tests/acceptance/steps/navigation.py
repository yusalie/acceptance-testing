from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome('/Users/Yusuf Salie/Downloads/chromedriver_win32 (1)/chromedriver')
    browser.get('http://127.0.0.1:5000')

@then('I am on blog page')
def step_impl(contex):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert contex.browser.current_url == expected_url
    
@given('I am on the blog page')
def step_impl(context):
    browser = webdriver.Chrome('/Users/Yusuf Salie/Downloads/chromedriver_win32 (1)/chromedriver')
    browser.get('http://127.0.0.1:5000/blog')

@then('I am on homepage')
def step_impl(contex):
    expected_url = 'http://127.0.0.1:5000/'
    assert contex.browser.current_url == expected_url