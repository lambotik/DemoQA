from locators.elements_page_locators import ButtonPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    # Actions

    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK))
        print('Double Clicked')
        return self.check_result_click(self.locators.DOUBLE_CLICK)

    def right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK))
        print('Right Clicked')
        return self.check_result_click(self.locators.RIGHT_CLICK)

    def click_me(self):
        self.action_one_click(self.element_is_visible(self.locators.CLICK_ME))
        print('Click Me Clicked')
        return self.check_result_click(self.locators.CLICK_ME)

    def check_result_click(self, output):
        print('Output Message: ', self.element_is_present(output).text)
        return self.element_is_present(output).text

    # Method
    def different_click_on_the_buttons(self):
        Logger.add_start_step(method='different_click_on_the_buttons')
        self.remove_footer()
        self.remove_fixedban()
        self.double_click()
        self.right_click()
        self.click_me()
        Logger.add_end_step(url=self.driver.current_url, method='different_click_on_the_buttons')
