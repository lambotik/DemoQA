import time

from generator.generator import generated_person
from locators.alert_frame_window_page_locators import AlertFrameWindowsPageLocators, AlertsPageLocators
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


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_alert_text(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        print('Click Button')
        alert_window = self.got_to_alert()
        print(alert_window.text)
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        print('Click Button')
        time.sleep(5)
        alert_window = self.got_to_alert()
        print(alert_window.text)
        return alert_window.text

    def check_confirm_alert(self):
        Logger.add_start_step(method='check_confirm_alert')
        self.element_is_visible(self.locators.CONFIRM_BUTTON_ALERT).click()
        print('Click Button')
        alert_window = self.got_to_alert()
        alert_window_text = alert_window.text
        alert_window.accept()
        print(alert_window_text)
        confirm_result = self.element_is_visible(self.locators.RESULT_CONFIRM_ALERT).text
        print(confirm_result)
        Logger.add_end_step(url=self.driver.current_url, method='check_confirm_alert')
        return confirm_result

    def check_promt_alert_result(self):
        Logger.add_start_step(method='check_promt_alert_result')
        person = next(generated_person())
        text = person.first_name
        self.element_is_visible(self.locators.LOGIN_ALERT_BUTTON).click()
        print('Click Button')
        alert_window = self.got_to_alert()
        alert_window_text = alert_window.text
        alert_window.send_keys(f'{text}')
        alert_window.accept()
        print(alert_window_text)
        confirm_result = self.element_is_visible(self.locators.PROMT_ALERT_RESULT).text
        confirm_result = confirm_result.split(' ')
        print(*confirm_result)
        print(f'Result entered {confirm_result[2]}')
        Logger.add_end_step(url=self.driver.current_url, method='check_promt_alert_result')
        return text, confirm_result[2]
