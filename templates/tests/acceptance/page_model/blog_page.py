import sys
sys.path.append("templates/tests/acceptance/page_models")
sys.path.append("templates/tests/acceptance/locators")

from page_model.base_page import BasePage
from locators.blog_page import BlogPageLocators

class BlogPage(BasePage):
  @property
  def url(self):
      return super(BlogPage, self).url + '/blog'
  
  @property
  def post_section(self):
      return self.driver.find_element(*BlogPageLocators.POST_SECTION)
  
  
  @property
  def posts(self):
      return self.driver.find_element(*BlogPageLocators.POST)
  
  @property
  def add_post_link(self):
      return self.driver.find_element(*BlogPageLocators.add_post_link)