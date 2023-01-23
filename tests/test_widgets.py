from pages.Widgets.widgets_page import AccordianPage


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
