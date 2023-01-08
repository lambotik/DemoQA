from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    # Actions

    """"Заполняет форму рандомными данными при помощи генератора и библиотеки faker.
    Возвращает данные внесенные в форму"""

    def fill_all_fields(self):
        # next обращается к generated_person() и возвращает по одному значению
        person_info = next(generated_person())
        full_name = person_info.full_name
        print(f'Generated Full Name is: {full_name}')
        email = person_info.email
        print(f'Generated Email is: {email}')
        current_address = person_info.current_address
        print(f'Generated Current Address is: {current_address}')
        permanent_address = person_info.permanent_address
        print(f'Generated Permanent Address is: {permanent_address}')
        self.element_is_visible(self.locators.INPUT_FULL_NAME).send_keys(full_name)
        print(f'Input Name: {full_name}')
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(email)
        print(f'Input Email: {email}')
        self.element_is_visible(self.locators.INPUT_CURRENT_ADDRESS).send_keys(current_address)
        print(f'Input Current Address: {current_address}')
        self.element_is_visible(self.locators.INPUT_PERMANENT_ADDRESS).send_keys(permanent_address)
        print(f'Input Permanent Address: {permanent_address}')
        self.elements_is_clickable(self.locators.BUTTON_SUBMIT).click()
        print('Click Submit')
        # костыль для обращения к input_data из другой функции
        global input_data
        input_data = full_name, email, current_address, permanent_address
        return full_name, email, current_address, permanent_address

    """Список введенных данных"""

    def get_input_data(self):
        list_input_data = str([i for i in input_data])
        # print(list_input_data)
        return list_input_data

    """Список данных отображенных в таблице"""

    def get_created_data(self):
        list_created_data = str([i for i in created_data])
        # print(list_created_data)
        return list_created_data

    """"Возвращает данные в созданной таблице"""

    def check_field_form_created(self):
        created_full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        print(f'Checked name in table: {created_full_name}')
        created_email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        print(f'Checked email in table: {created_email}')
        created_current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        print(f'Checked current Address in table: {created_current_address}')
        created_permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        print(f'Checked permanent Address in table: {created_permanent_address}')
        global created_data
        created_data = created_full_name, created_email, created_current_address, created_permanent_address
        return created_full_name, created_email, created_current_address, created_permanent_address

    # Methods

    def assert_fill_all_fields_and_check_output_in_table(self):
        Logger.add_start_step(method='assert_fill_all_fields_and_check_output_in_table')
        self.remove_footer()
        self.remove_fixedban()
        full_name, email, current_address, permanent_address = self.fill_all_fields()
        created_full_name, created_email, created_current_address, created_permanent_address = self.check_field_form_created()
        assert full_name == created_full_name, 'Not Correct Full Name'
        assert email == created_email, 'Not Correct Email'
        assert current_address == created_current_address, 'Not Correct Current Address'
        assert permanent_address == created_permanent_address, 'Not Correct Permanent Address'
        assert self.get_input_data() == self.get_created_data(), 'Input data and Created data is not equal'
        Logger.add_end_step(url=self.driver.current_url, method='assert_fill_all_fields_and_check_output_in_table')
