import time

from selenium.common import TimeoutException

from locators.elements_page_locators import DynamicPropertiesPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_enable_button(self):
        Logger.add_start_step(method='check_enable_button')
        try:
            print('Checking if an element is enable')
            self.elements_is_clickable(self.locators.ENABLE_AFTER_BUTTON).click()
            Logger.add_end_step(url=self.driver.current_url, method='check_enable_button')
        except TimeoutException:
            return False
        return True

    def check_appear_button(self):
        Logger.add_start_step(method='check_appear_button')
        try:
            print('Checking if an element is visible')
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
            Logger.add_end_step(url=self.driver.current_url, method='check_appear_button')
        except TimeoutException:
            return False
        return True

    def check_changed_of_color(self):
        Logger.add_start_step(method='check_changed_of_color')
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        print('Initial button color: ', color_button_before)
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        print('Button color after clicking: ', color_button_after)
        Logger.add_end_step(url=self.driver.current_url, method='check_changed_of_color')
        return color_button_before, color_button_after
