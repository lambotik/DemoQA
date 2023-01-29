import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date, generated_time_through_15_minutes
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators
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


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def check_entered_date(self):
        Logger.add_start_step(method='check_entered_date')
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        len_date = len((input_date.get_attribute('value')))
        input_date.send_keys(Keys.BACKSPACE * len_date)
        entered_date = '03/15/1988'
        input_date.send_keys(entered_date, Keys.RETURN)
        print(f'Entered date: {entered_date}')
        result_date = input_date.get_attribute('value')
        print(f'Result date: {result_date}')
        Logger.add_end_step(url=self.driver.current_url, method='check_entered_date')
        return entered_date, result_date

    def select_date(self):
        Logger.add_start_step(method='select_date')
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        print('Date before: ', value_date_before)
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        input_date_after = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        print('Date After: ', value_date_after)
        Logger.add_end_step(url=self.driver.current_url, method='select_date')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        Logger.add_start_step(method='select_date_and_time')
        date = next(generated_date())
        set_time = next(generated_time_through_15_minutes())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        print('Date before: ', value_date_before)
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, random.choice(set_time.time_15))
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        print('Date After: ', value_date_after)
        Logger.add_end_step(url=self.driver.current_url, method='select_date_and_time')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        Logger.add_start_step(method='change_slider_value')
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        print(f'Value before: {value_before}')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        print(f'Value after: {value_after}')
        Logger.add_end_step(url=self.driver.current_url, method='change_slider_value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def check_progress_bar_value(self):
        Logger.add_start_step(method='check_progress_bar_value')
        value_before_start = self.element_is_visible(self.locators.PROGRESS_BAR).text
        print('Value before start: ', value_before_start)
        click_start = self.element_is_visible(self.locators.START_AND_STOP_BUTTON)
        click_start.click()
        print('Click start')
        time.sleep(random.randint(1, 5))
        click_stop = self.element_is_visible(self.locators.START_AND_STOP_BUTTON)
        click_stop.click()
        print('Click stop')
        value_after_stop = self.element_is_visible(self.locators.PROGRESS_BAR).text
        print('Value after stop: ', value_after_stop)
        Logger.add_end_step(url=self.driver.current_url, method='check_progress_bar_value')
        return value_before_start, value_after_stop


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_title(self, name_tab):
        title = self.element_is_visible(name_tab)
        return title.text

    def get_len_text(self):
        len_text = len(self.element_is_visible(self.locators.TAB_CONTENT).text)
        return len_text

    def check_what_tab(self):
        title = self.check_title(self.locators.TAB_WHAT)
        self.element_is_visible(self.locators.TAB_WHAT).click()
        len_text = self.get_len_text()
        print(f'Title name is: {title}')
        print(f'Length text is: {len_text}')
        return title, len_text

    def check_origin_tab(self):
        title = self.check_title(self.locators.TAB_ORIGIN)
        self.element_is_visible(self.locators.TAB_ORIGIN).click()
        len_text = self.get_len_text()
        print(f'Title name is: {title}')
        print(f'Length text is: {len_text}')
        return title, len_text

    def check_use_tab(self):
        title = self.check_title(self.locators.TAB_USE)
        self.element_is_visible(self.locators.TAB_USE).click()
        len_text = self.get_len_text()
        print(f'Title name is: {title}')
        print(f'Length text is: {len_text}')
        return title, len_text

    def check_more_tab(self):
        title = self.check_title(self.locators.TAB_MORE)
        self.element_is_visible(self.locators.TAB_MORE).click()
        len_text = self.get_len_text()
        print(f'Title name is: {title}')
        print(f'Length text is: {len_text}')
        return title, len_text

