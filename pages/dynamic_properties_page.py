import time

from selenium.common import TimeoutException

from locators.elements_page_locators import DynamicPropertiesPageLocators
from pages.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    # Actions

    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        print('Initial button color: ', color_button_before)
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        print('Button color after clicking: ', color_button_after)
        return color_button_before, color_button_after

    def check_appear_button(self):
        try:
            print('Checking if an element is visible')
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_enable_button(self):
        try:
            print('Checking if an element is enable')
            self.elements_is_clickable(self.locators.ENABLE_AFTER_BUTTON).click()
        except TimeoutException:
            return False
        return True
