import random

from selenium.webdriver.common.by import By

from locators.elements_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    # Actions

    """Открывает весь список чек боксов"""

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()
        print('Click Button Expand All List')

    """Выполняем рандомные клики по чек боксам"""

    def click_random_check_box(self):
        item_list = self.elements_are_visible(self.locators.TITLE_LIST)
        count = 21
        print('Randomly select checkbox')
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                # print('Click Random Check Box:', item.text)
                count -= 1

            else:
                print(item)
                break

    """"Получаем выбранные чек боксы"""

    def get_checked_check_boxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_LIST_TEXT)
            data.append(title_item.text)
        data = str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        print('Formatting data for the titles of selected checkboxes')
        print(f'List of selected checkboxes: {data}')
        return data

    """"Получаем список отображенных чек боксов и форматируем для сравнения"""

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        data = str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        print('Formatting data for the result titles of selected checkboxes')
        print(f'List of selected checkbox titles: {data}')
        return data

    def assert_checkbox_input_and_output(self):
        input_checkboxes = self.get_checked_check_boxes()
        output_checkboxes = self.get_output_result()
        print('Comparing the results')
        assert input_checkboxes == output_checkboxes, 'Not correct checked checkboxes result'

    # Methods

    def check_box(self):
        Logger.add_start_step(method='check_box')
        self.remove_footer()
        self.remove_fixedban()
        self.open_full_list()
        self.click_random_check_box()
        self.assert_checkbox_input_and_output()
        Logger.add_end_step(url=self.driver.current_url, method='check_box')
