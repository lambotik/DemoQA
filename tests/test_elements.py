import time
import datetime
import pytest

import utilities
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage


class TestElements:

    class TestTextBox:

        def test_elements(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.remove_footer()
            text_box_page.remove_fixedban()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            created_full_name, created_email, created_current_address, created_permanent_address = text_box_page.check_field_form_created()
            assert full_name == created_full_name, 'Not Correct Full Name'
            assert email == created_email, 'Not Correct Email'
            assert current_address == created_current_address, 'Not Correct Current Address'
            assert permanent_address == created_permanent_address, 'Not Correct Permanent Address'
            assert text_box_page.get_input_data() == text_box_page.get_created_data(), 'Input data and Created data is not equal'

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
        def test_web_table_at_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_person = web_table_page.check_added_new_person()
            print('Compare whether the created data appeared in the table')
            assert new_person in table_person, 'Created data is not in the table'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.add_new_person()
            web_table_page.check_added_new_person()
            random_key_word = web_table_page.selected_random_keyword()
            web_table_page.search_some_person(f'{random_key_word}')
            table_result = web_table_page.check_search_person()
            # print(f'random key word: {random_key_word}')
            # print(f'table result: {table_result}')
            assert random_key_word in table_result, 'The Person Was Not Found In The Table'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_fixedban()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            edit_person_data = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            for edit_person_data in str(row):
                assert str(edit_person_data) in str(row), f'Updated element {edit_person_data} not in the table'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_fixedban()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person(f'{email}')
            text = web_table_page.check_deleted()
            assert text == 'No rows found', f'{email} Person have not deleted'

        def test_change_the_number_of_line(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_fixedban()
            web_table_page.remove_footer()
            count = web_table_page.change_the_number_of_line()
            assert count == [5, 10, 20, 25, 50, 100]

    class TestButton():

        def test_different_click_on_the_buttons(self, driver, set_group):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            button_page.remove_footer()
            button_page.remove_fixedban()
            button_page.different_click_on_the_buttons()
