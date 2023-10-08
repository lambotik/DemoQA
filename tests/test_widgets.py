import allure
import pytest

from pages.Widgets.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, \
    TabsPage, ToolsTipsPage, MenuPage

@allure.suite('Test Widgets Page')
class TestWidgetsPage:
    @allure.feature('Test Accordian')
    class TestAccordian:
        @allure.step('Check accordian title and content')
        @pytest.mark.xfail
        def test_accordian_title_and_content(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            firs_tab_title, first_tab_content = accordian_page.check_accordian('first')
            second_tab_title, second_tab_content = accordian_page.check_accordian('second')
            third_tab_title, third_tab_content = accordian_page.check_accordian('third')
            assert firs_tab_title == 'What is Lorem Ipsum?' and first_tab_content > 0
            assert second_tab_title == 'Where does it come from?' and second_tab_content > 0
            assert third_tab_title == 'Why do we use it?' and third_tab_content > 0

    @allure.feature('Test Auto Complete')
    class TestAutoComplete:
        @allure.step('Check fill multi auto complete')
        def test_fill_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_multi()
            colors = auto_complete_page.check_color_in_multi()
            assert color == colors, 'The added colors are missing in the input'

        @allure.step('Check remove all colors')
        def test_remove_all_colors(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'Values did not deleted'

        @allure.step('Check fill single complete')
        def test_fill_single_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color, color_result = auto_complete_page.fill_input_single()
            assert color == color_result, 'The added color are missing in the input'

    @allure.feature('Test Date Picker')
    class TestDatePicker:
        @allure.step('Check check entered date')
        def test_check_entered_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            entered_date, result_date = date_picker_page.check_entered_date()
            assert entered_date == result_date, 'Entered date not equal result'

        @allure.step('Check select date')
        @pytest.mark.xfail
        def test_select_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'The date has not been changed'

        @allure.step('Check select date and time')
        def test_select_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, 'The date and time has not been changed'

    @allure.feature('Test Slider')
    class TestSlider:
        @allure.step('Check change slider value')
        def test_change_slider_value(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after, 'The value slider has not been change'

    @allure.feature('Test Progress Bar')
    class TestProgressBar:
        @allure.step('Check progress bar value')
        def test_progress_bar_value(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value_before, value_after = progress_bar_page.check_progress_bar_value()
            assert value_before != value_after, 'The value progress bar has not been change'

    @allure.feature('Test Tabs')
    class TestTabs:
        @allure.step('Check what tab')
        def test_what_tab(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tab_title, length_text = tabs_page.check_what_tab()
            assert tab_title == 'What', 'Title does not match'
            assert length_text > 0, 'Text is missing'

        @allure.step('Check origin tab')
        def test_origin_tab(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tab_title, length_text = tabs_page.check_origin_tab()
            assert tab_title == 'Origin', 'Title does not match'
            assert length_text > 0, 'Text is missing'

        @allure.step('Check use tab')
        def test_use_tab(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tab_title, length_text = tabs_page.check_use_tab()
            assert tab_title == 'Use', 'Title does not match'
            assert length_text > 0, 'Text is missing'

        @allure.step('Check more tab')
        @pytest.mark.xfail
        def tes_more_tab(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tab_title, length_text = tabs_page.check_more_tab()
            assert tab_title == 'More', 'Title does not match'
            assert length_text > 0, 'Text is missing'

    @allure.feature('Test Tools Tips')
    class TestToolsTips:
        @allure.step('Check message after hover to button')
        def test_message_after_hover_to_button(self, driver):
            tools_tips_page = ToolsTipsPage(driver, 'https://demoqa.com/tool-tips')
            tools_tips_page.open()
            message_after_hover = tools_tips_page.check_message_after_hover_to_button()
            assert message_after_hover == 'You hovered over the Button', 'Hover missing or incorrect content'

        @allure.step('Check message after hover to input')
        def test_message_after_hover_to_input(self, driver):
            tools_tips_page = ToolsTipsPage(driver, 'https://demoqa.com/tool-tips')
            tools_tips_page.open()
            message_after_hover = tools_tips_page.check_message_after_hover_to_input()
            assert message_after_hover == 'You hovered over the text field', 'Hover missing or incorrect content'

        @allure.step('Check message after hover to text')
        def test_message_after_hover_to_text(self, driver):
            tools_tips_page = ToolsTipsPage(driver, 'https://demoqa.com/tool-tips')
            tools_tips_page.open()
            message_after_hover = tools_tips_page.check_message_after_hover_to_text()
            assert message_after_hover == 'You hovered over the Contrary', 'Hover missing or incorrect content'

        @allure.step('Check message after hover to digit')
        def test_message_after_hover_to_digit(self, driver):
            tools_tips_page = ToolsTipsPage(driver, 'https://demoqa.com/tool-tips')
            tools_tips_page.open()
            message_after_hover = tools_tips_page.check_message_after_hover_to_digit()
            assert message_after_hover == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'

        @allure.step('Check all tool tips')
        def test_all_tool_tips(self, driver):
            tools_tips_page = ToolsTipsPage(driver, 'https://demoqa.com/tool-tips')
            tools_tips_page.open()
            button, input_field, text, digit = tools_tips_page.check_all_tool_tips()
            assert button == 'You hovered over the Button', 'Hover missing or incorrect content'
            assert input_field == 'You hovered over the text field', 'Hover missing or incorrect content'
            assert text == 'You hovered over the Contrary', 'Hover missing or incorrect content'
            assert digit == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'

    @allure.feature('Test Menu')
    class TestMenu:
        @allure.step('Check menu tabs and subtabs')
        def test_menu_tabs_and_subtabs(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu_tabs_and_subtabs()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], 'Menu items do not exist or have nit been selected'
