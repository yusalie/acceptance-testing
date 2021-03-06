from behave import *
import sys
sys.path.append("templates/tests")
from selenium import webdriver
from acceptance.page_model.home_page import HomePage
from acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome('/Users/Yusuf Salie/Downloads/chromedriver_win32 (1)/chromedriver')
    page = HomePage(context.driver)
    context.driver(page.url)

@then('I am on new post page')
def step_impl(contex):
    contex.driver = webdriver.Chrome('/Users/Yusuf Salie/Downloads/chromedriver_win32 (1)/chromedriver')
    page = NewPostPage(contex.driver)
    contex.driver.get(page.url)
    
    
@given('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(contex.driver).current
    assert context.driver.current_url == expected_url

@then('I am on homepage')
def step_impl(contex):
    expected_url = HomePage(context.driver).url
    assert contex.browser.current_url == expected_url