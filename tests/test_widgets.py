from pages.Widgets.widgets_page import AccordianPage, AutoCompletePage


class TestWidgetsPage:
    class TestAccordian:

        def test_accordian_title_and_content(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            firs_tab_title, first_tab_content = accordian_page.check_accordian('first')
            second_tab_title, second_tab_content = accordian_page.check_accordian('second')
            third_tab_title, third_tab_content = accordian_page.check_accordian('third')
            assert firs_tab_title == 'What is Lorem Ipsum?' and first_tab_content > 0
            assert second_tab_title == 'Where does it come from?' and second_tab_content > 0
            assert third_tab_title == 'Why do we use it?' and third_tab_content > 0

    class TestAutoComplete:

        def test_fill_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_multi()
            colors = auto_complete_page.check_color_in_multi()
            assert color == colors, 'The added colors are missing in the input'

        def test_remove_all_colors(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'Values did not deleted'

        def test_fill_single_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color, color_result = auto_complete_page.fill_input_single()
            assert color == color_result, 'The added color are missing in the input'
