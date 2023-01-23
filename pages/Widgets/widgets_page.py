from selenium.common import TimeoutException

from locators.widgets_locators import AccordianPageLocators
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
