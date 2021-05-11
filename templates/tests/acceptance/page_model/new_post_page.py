from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.locators.new_post_page import NewPostPageLocator

class NewPostPage(BasePage):
  @property
  def url(self):
      return super(NewPostPage, self).url + '/post'
  
  @property
  def form(self):
      return self.driver.find_element(*NewPostPageLocator.NEW_POST_FORM)
  
  @property
  def submit_button(self):
      return self.driver.find_element(*NewPostPageLocator.SUBMIT_BUTTON)
  
  def from_field(self):
      return self.form.find_element(By.NAME, name)
  
  