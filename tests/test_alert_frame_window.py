import time
import pytest

from pages.alerts_frame_windows_page import AlertFrameWindowsPage


class TestAlertFrameWindowsPage:
    class TestAlertFrameWindows:
        def test_new_tab(self, driver):
            browser_windows_page = AlertFrameWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            page_text = browser_windows_page.check_new_tab_page()
            assert page_text == 'This is a sample page', 'Wrong text on the page'

        def test_new_window_page(self, driver):
            browser_windows_page = AlertFrameWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            page_text = browser_windows_page.check_new_window_page()
            assert page_text == 'This is a sample page', 'Wrong text on the page'
