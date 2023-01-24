import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        Logger.add_start_step(method='check_accordian')
        accordian = {'first':
                         {'title': self.locators.FIRST_TAB,
                          'content': self.locators.FIRST_TAB_TEXT},
                     'second':
                         {'title': self.locators.SECOND_TAB,
                          'content': self.locators.SECOND_TAB_TEXT},
                     'third':
                         {'title': self.locators.THIRD_TAB,
                          'content': self.locators.THIRD_TAB_TEXT},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        print(f'Selected tab: {section_title.text}')
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
            print(f'Content length:{len(section_content)}')
        except TimeoutException:
            section_title.click()
            print(f'Selected tab: {section_title.text}')
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
            print(f'Content length:{len(section_content)}')
        Logger.add_end_step(url=self.driver.current_url, method='check_accordian')
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        """random.sample chooses k=num elements from the list"""
        Logger.add_start_step(method='fill_input_multi')
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.elements_is_clickable(self.locators.INPUT_MULTI)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        print(f'Selected colors: {colors}')
        Logger.add_end_step(url=self.driver.current_url, method='fill_input_multi')
        return colors

    def remove_value_from_multi(self):
        Logger.add_start_step(method='remove_value_from_multi')
        count_value_before = len(self.elements_are_present(self.locators.LIST_MULTI_VALUE))
        print(f'Count value before: {count_value_before}')
        remove_button_list = self.elements_are_visible(self.locators.CLOSE_MULTI_VALUE_ELEMENT)
        try:
            while True:
                for value in remove_button_list:
                    value.click()
                break
            count_value_after = 0
        except TimeoutException:
            count_value_after = self.element_is_visible(self.locators.LIST_MULTI_VALUE)
        print(f'Count value after: {count_value_after}')
        Logger.add_end_step(url=self.driver.current_url, method='remove_value_from_multi')
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        Logger.add_start_step(method='check_color_in_multi')
        color_list = self.elements_are_present(self.locators.LIST_MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        print(f'Added colors: {colors}')
        Logger.add_end_step(url=self.driver.current_url, method='check_color_in_multi')
        return colors

    def fill_input_single(self):
        Logger.add_start_step(method='fill_input_single')
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.elements_is_clickable(self.locators.INPUT_SINGLE)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        print(f'Selected color: {color}')
        color_result = self.element_is_visible(self.locators.SINGLE_CONTAINER).text
        print(f'Color result: {color_result}')
        Logger.add_end_step(url=self.driver.current_url, method='fill_input_single')
        return *color, color_result

