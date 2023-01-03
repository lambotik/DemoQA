import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage


class TestElements:
    class TestTextBox:

        def test_fill_all_fields_and_check_output_in_table(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.assert_fill_all_fields_and_check_output_in_table()

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.check_box()

    class TestRadioButton:
        @pytest.mark.xfail
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.radio_button()

    class TestWebTable:
        def test_web_table_add_new_person_and_check_this(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.web_table_add_new_person_and_check_this()

        def test_web_table_search_added_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.web_table_search_added_person()

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.web_table_update_person_info()

        def test_remove_person_from_web_table_and_check_this(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_person_from_web_table_and_check_this()

        @pytest.mark.xfail
        def test_change_the_number_of_rows_and_count_them(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.change_the_number_of_rows_and_count_them()

    class TestButton:

        def test_different_click_on_the_buttons(self, driver, set_group):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            button_page.different_click_on_the_buttons()

    class TestLinks:

        def test_home_link_response_code_200(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_response_code_200()
        @pytest.mark.xfail
        def test_bad_request_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_bad_response()

        @pytest.mark.xfail
        def test_created_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_created_response()

        @pytest.mark.xfail
        def test_no_content_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_no_content_response()

        @pytest.mark.xfail
        def test_moved_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_moved_response()

        @pytest.mark.xfail
        def test_unauthorized_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_unauthorized_response()

        @pytest.mark.xfail
        def test_forbidden_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_forbidden_response()

        @pytest.mark.xfail
        def test_not_found_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_not_found_response()

