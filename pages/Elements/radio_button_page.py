from locators.elements_page_locators import RadioButtonPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'Yes': self.locators.YES_BUTTON,
                   'Impressive': self.locators.IMPRESSIVE_BUTTON,
                   'No': self.locators.NO_BUTTON}
        self.element_is_visible(choices[choice]).click()
        print(f'Click Radio Button: {choice}')

    def get_output_result(self):
        output_result = self.element_is_present(self.locators.OUTPUT_TEXT_RESULT).text
        print(f'Output result message: {output_result}')
        return output_result

    def radio_button(self):
        Logger.add_start_step(method='radio_button')
        print('Select <Yes>')
        self.click_on_the_radio_button('Yes')
        output_yes = self.get_output_result()
        print(f'Output result <{output_yes}>')
        print('Compare result')
        assert output_yes == 'Yes', '<Yes> has not been selected'
        print('Select <Impressive>')
        self.click_on_the_radio_button('Impressive')
        output_impressive = self.get_output_result()
        print(f'Output result <{output_impressive}>')
        print('Compare result')
        assert output_impressive == 'Impressive', '<Impressive> has not been selected'
        print('Select <No>')
        self.click_on_the_radio_button('No')
        output_no = self.get_output_result()
        print(f'Output result <{output_no}>')
        print('Compare result')
        assert output_no == 'No', '<No> has not been selected'
        Logger.add_end_step(url=self.driver.current_url, method='radio_button')
