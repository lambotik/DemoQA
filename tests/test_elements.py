import allure
import pytest

from pages.Elements.button_page import ButtonPage
from pages.Elements.check_box_page import CheckBoxPage
from pages.Elements.dynamic_properties_page import DynamicPropertiesPage
from pages.Elements.links_page import LinksPage
from pages.Elements.radio_button_page import RadioButtonPage
from pages.Elements.text_box_page import TextBoxPage
from pages.Elements.upload_and_download_page import UploadAndDownloadPage
from pages.Elements.web_table_page import WebTablePage


@allure.suite('Elements')
class TestElements:
    @allure.feature('Text Box')
    class TestTextBox:
        @allure.step('Check Text Box')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.assert_fill_all_fields_and_check_output_in_table()

    @allure.feature('Test CheckBox')
    class TestCheckBox:
        @allure.step('Check CheckBox')
        @pytest.mark.xfail
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.check_box()

    @allure.feature('Test RadioButton')
    class TestRadioButton:
        @allure.step('Check radio button')
        @pytest.mark.xfail
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.radio_button()

    @allure.feature('Test Web Table')
    class TestWebTable:
        @allure.step('Check web table add new person and check this')
        def test_web_table_add_new_person_and_check_this(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.web_table_add_new_person_and_check_this()

        @allure.step('Check web table search added person')
        def test_web_table_search_added_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.web_table_search_added_person()

        @allure.step('Check web table update person info')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.web_table_update_person_info()

        @allure.step('Check remove person from web table and check this')
        def test_remove_person_from_web_table_and_check_this(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.remove_person_from_web_table_and_check_this()

        @allure.step('Check change the number of rows and count them')
        @pytest.mark.xfail
        def test_change_the_number_of_rows_and_count_them(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.change_the_number_of_rows_and_count_them()

    @allure.feature('Test Button')
    class TestButton:
        @allure.step('Check different click on the buttons')
        def test_different_click_on_the_buttons(self, driver, set_group):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            button_page.different_click_on_the_buttons()

    @allure.feature('Test Links')
    class TestLinks:
        @allure.step('Check home link response code 200')
        def test_home_link_response_code_200(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_response_code_200()

        @allure.step('Check bad request link response code')
        def test_bad_request_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_bad_response()

        @allure.step('Check created link response code')
        def test_created_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_created_response()

        @allure.step('Check no content link response code')
        def test_no_content_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_no_content_response()

        @allure.step('Check moved link response code')
        def test_moved_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_moved_response()

        @allure.step('Check unauthorized link response code')
        def test_unauthorized_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_unauthorized_response()

        @allure.step('Check forbidden link response code')
        def test_forbidden_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_forbidden_response()

        @allure.step('Check not found link response code')
        def test_not_found_link_response_code(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_link_not_found_response()

    @allure.feature('Test Upload And Download')
    class TestUploadAndDownload:
        @allure.step('Check file upload check')
        def test_file_upload_check(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            file_name, result = upload_and_download_page.upload_file()
            assert file_name == result, 'The name of the uploaded file does not match the result'

        @allure.step('Check download file check')
        def test_download_file_check(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            upload_and_download_page.download_file_check()

    @allure.feature('Test Dynamic Properties Page')
    class TestDynamicPropertiesPage:
        @allure.step('Check dynamic properties change color')
        @pytest.mark.xfail
        def test_dynamic_properties_change_color(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_before != color_after, 'Button color has not changed'

        @allure.step('Check appear button')
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True, 'Button did not appear after 5 seconds'

        @allure.step('Check enable button')
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'Button did not enable after 5 seconds'
