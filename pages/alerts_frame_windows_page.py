from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from locators.alert_frame_window_page_locators import AlertFrameWindowsPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class AlertFrameWindowsPage(BasePage):
    locators = AlertFrameWindowsPageLocators()

    def check_new_tab_page(self):
        Logger.add_start_step(method='check_new_tab_page')
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        print('Click New Tab Button')
        self.got_to_a_new_tab()
        page_text = self.element_is_visible(self.locators.SAMPLE_PAGE).text
        print(page_text)
        Logger.add_end_step(url=self.driver.current_url, method='check_new_tab_page')
        return page_text

    def check_new_window_page(self):
        Logger.add_start_step(method='check_new_window_page')
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        print('Click New Tab Button')
        self.got_to_a_new_tab()
        page_text = self.element_is_visible(self.locators.SAMPLE_PAGE).text
        print(page_text)
        Logger.add_end_step(url=self.driver.current_url, method='check_new_window_page')
        return page_text
