from pages.alerts_frame_windows_page import AlertFrameWindowsPage, AlertsPage


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

    class TestAlert:
        def test_check_alert_text(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_text()
            assert alert_text == 'You clicked a button', 'Alert is not present'

        def test_check_alert_appear_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'You do not press OK on the ' \
                                                                        'alert window after 5 second'

        def test_check_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', 'You do not press OK on the alert window'

        def test_check_promt_alert_result(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            send_text, result_text = alerts_page.check_promt_alert_result()
            assert send_text == result_text, 'The entered text in the alert ' \
                                             'window does not match the result'
