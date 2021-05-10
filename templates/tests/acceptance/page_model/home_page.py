from tests.acceptance.locators.home_page import HomePageLocator
from tests.acceptance.page_model.base_page import BasePage

class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self.url + '/')
    
    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocator.NAVIGATION_LINK)