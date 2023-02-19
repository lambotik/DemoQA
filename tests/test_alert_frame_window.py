import allure

from pages.Alerts_Frame_Windows.alerts_frame_windows_page import AlertFrameWindowsPage, AlertsPage, FramePage, \
    NestedFramePage, \
    ModalDialogPage

@allure.suite('Test Alert Frame Windows Page')
class TestAlertFrameWindowsPage:
    @allure.feature('Test Alert Frame Windows Page')
    class TestAlertFrameWindowsPage:
        @allure.step('Check new tab')
        def test_new_tab(self, driver):
            browser_windows_page = AlertFrameWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            page_text = browser_windows_page.check_new_tab_page()
            assert page_text == 'This is a sample page', 'Wrong text on the page'

        @allure.step('Check new window page')
        def test_new_window_page(self, driver):
            browser_windows_page = AlertFrameWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            page_text = browser_windows_page.check_new_window_page()
            assert page_text == 'This is a sample page', 'Wrong text on the page'

    @allure.feature('Test Alert Page')
    class TestAlertPage:
        @allure.step('Check check alert text')
        def test_check_alert_text(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_text()
            assert alert_text == 'You clicked a button', 'Alert is not present'

        @allure.step('Check alert appear 5 sec')
        def test_check_alert_appear_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'You do not press OK on the ' \
                                                                        'alert window after 5 second'

        @allure.step('Check confirm alert')
        def test_check_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', 'You do not press OK on the alert window'

        @allure.step('Check promt alert result')
        def test_check_promt_alert_result(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            send_text, result_text = alerts_page.check_promt_alert_result()
            assert send_text == result_text, 'The entered text in the alert ' \
                                             'window does not match the result'

    @allure.feature('Test Frames Page')
    class TestFramesPage:
        @allure.step('Check frame size')
        def test_frame_size(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame_1 = frame_page.check_frame_size('frame1')
            result_frame_2 = frame_page.check_frame_size('frame2')
            assert result_frame_1 == ['This is a sample page', '500px', '350px'], 'The frame 1 does not exist'
            assert result_frame_2 == ['This is a sample page', '100px', '100px'], 'The frame 2 does not exist'

    @allure.feature('Test Nested Frames Page')
    class TestNestedFramesPage:
        @allure.step('Check nested frame')
        def test_nested_frame(self, driver):
            nested_frame_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_frame, child_frame = nested_frame_page.check_nested_frame()
            assert parent_frame == 'Parent frame', 'Parent frame has not been present'
            assert child_frame == 'Child Iframe', 'Child frame has not been present'

    @allure.feature('Test Modal Dialog Page')
    class TestModalDialogPage:
        @allure.step('Check small modal window text')
        def test_small_modal_window_text(self, driver):
            modal_dialog_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            modal_title, modal_text = modal_dialog_page.check_the_text_of_the_small_modal_window()
            assert modal_title == 'Small Modal', 'Invalid title text'
            assert modal_text == 'This is a small modal. It has very less content', 'Invalid modal window text'

        @allure.step('Check large modal window text')
        def test_large_modal_window_text(self, driver):
            modal_dialog_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            modal_title, modal_text = modal_dialog_page.check_the_text_of_the_large_modal_window()
            assert modal_title == 'Large Modal', 'Invalid title text'
            assert modal_text == 574, 'Incorrect text length'
