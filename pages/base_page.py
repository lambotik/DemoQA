import random

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        with allure.step(f'Check if the {locator} is visible on the page'):
            if self.go_to_element(self.element_is_present(locator)) != True:
                self.attach_screenshot(locator)
                return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            raise f'{locator} dose not visible\n {locator} Searching by: {locator[0]}\n Selector: {locator[1]}'
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def elements_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_enter_to_element(self, locator, timeout=5):
        wait(self.driver, timeout).until(EC.element_to_be_clickable(locator(Keys.RETURN)))

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        print('\nRemove Footer')

    """"Данный метод убирает рекламный банер"""

    def remove_fixedban(self):
        self.driver.execute_script("document.getElementById('fixedban').style.display = 'none'")
        print('Remove Fixedban')

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def action_one_click(self, element):
        action = ActionChains(self.driver)
        action.click(element).perform()

    def got_to_a_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def got_to_alert(self):
        return self.driver.switch_to.alert

    def go_to_frame(self, element):
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def random_choice_from_elements_list(self, elements_list_locator):
        empty_list = []
        full_list = self.elements_are_present(elements_list_locator)
        for t in full_list:
            empty_list.append(t.text)
        return random.choice(full_list)

    def action_drag_and_drop_offset(self, element, x_coord, y_coord):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_drag_and_drop_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def attach_screenshot(self, element):
        """Create screenshot of current window and attach it in allure report
        Args:
         - file_name: str like 'Linkedin_button_not_found'
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=element, attachment_type=AttachmentType.PNG)
