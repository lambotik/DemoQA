import time

from generator.generator import generated_person
from locators.alert_frame_window_page_locators import AlertFrameWindowsPageLocators, AlertsPageLocators, \
    FramePageLocators, NestedFramePageLocators, ModalDialogPageLocators
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


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame_size(self, frame_num):
        Logger.add_start_step(method='check_frame_size')
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.BIG_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            print('Frame 1 width:', width, '\n''Frame 1 height:', height)
            self.go_to_frame(frame)
            text = self.element_is_visible(self.locators.TITLE_FRAME).text
            print(f'Frame 1 text: {text}')
            self.switch_to_default_content()
            Logger.add_end_step(url=self.driver.current_url, method='check_frame_size')
            return [text, width, height]
        Logger.add_start_step(method='check_frame_size')
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SMALL_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            print('Frame 2 width:', width, '\n''Frame 2 height:', height)
            self.go_to_frame(frame)
            text = self.element_is_visible(self.locators.TITLE_FRAME).text
            print(f'Frame 2 text: {text}')
            self.switch_to_default_content()
            Logger.add_end_step(url=self.driver.current_url, method='check_frame_size')
            return [text, width, height]


class NestedFramePage(BasePage):
    locators = NestedFramePageLocators()

    def check_nested_frame(self):
        Logger.add_start_step(method='check_nested_frame')
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.go_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        print(f'Parent frame text: {parent_text}')
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.go_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        print(f'Child frame text: {child_text}')
        Logger.add_end_step(url=self.driver.current_url, method='check_nested_frame')
        return parent_text, child_text


class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()

    def check_the_text_of_the_small_modal_window(self):
        Logger.add_start_step(method='check_the_text_of_the_small_modal_window')
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        print('Click Small Modal')
        modal_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        modal_text = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        print(f'Modal Title: {modal_title}\nModal Text: {modal_text}')
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL).click()
        print('Click Close Modal')
        Logger.add_end_step(url=self.driver.current_url, method='check_the_text_of_the_small_modal_window')
        return modal_title, modal_text

    def check_the_text_of_the_large_modal_window(self):
        Logger.add_start_step(method='check_the_text_of_the_large_modal_window')
        self.element_is_visible(self.locators.LARGE_MODAL).click()
        print('Click Large Modal')
        modal_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        modal_text = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text
        self.element_is_visible(self.locators.CLOSE_LARGE_MODAL).click()
        print(f'Modal Title: {modal_title}\nModal Text Length: {len(modal_text)}')
        print('Click Close Modal')
        Logger.add_end_step(url=self.driver.current_url, method='check_the_text_of_the_large_modal_window')
        return modal_title, len(modal_text)
