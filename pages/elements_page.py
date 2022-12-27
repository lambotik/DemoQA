import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonPageLocators
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

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    # Actions

    """Открывает весь список чек боксов"""

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()
        print('Click Button Expand All List')

    """Выполняем рандомные клики по чек боксам"""

    def click_random_check_box(self):
        item_list = self.elements_are_visible(self.locators.TITLE_LIST)
        count = 21
        print('Randomly select checkbox')
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                # print('Click Random Check Box:', item.text)
                count -= 1

            else:
                print(item)
                break

    """"Получаем выбранные чек боксы"""

    def get_checked_check_boxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_LIST_TEXT)
            data.append(title_item.text)
        data = str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        print('Formatting data for the titles of selected checkboxes')
        print(f'List of selected checkboxes: {data}')
        return data

    """"Получаем список отображенных чек боксов и форматируем для сравнения"""

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        data = str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        print('Formatting data for the result titles of selected checkboxes')
        print(f'List of selected checkbox titles: {data}')
        return data

    def assert_checkbox_input_and_output(self):
        input_checkboxes = self.get_checked_check_boxes()
        output_checkboxes = self.get_output_result()
        print('Comparing the results')
        assert input_checkboxes == output_checkboxes, 'Not correct checked checkboxes result'

    # Methods

    def check_box(self):
        Logger.add_start_step(method='check_box')
        self.remove_footer()
        self.remove_fixedban()
        self.open_full_list()
        self.click_random_check_box()
        self.assert_checkbox_input_and_output()
        Logger.add_end_step(url=self.driver.current_url, method='check_box')


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


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    # Actions

    def add_new_person(self):
        count = 1
        # count = random.randint(1, 3)
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            print('Click Add Button')
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            print(f'Input First Name: {first_name}')
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            print(f'Input Last Name: {last_name}')
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            print(f'Input Email: {email}')
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            print(f'Input Age: {age}')
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            print(f'Input Salary: {salary}')
            self.element_is_visible(self.locators.DEPARTAMENT_INPUT).send_keys(department)
            print(f'Input Department: {department}')
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_new_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        print('Get A List Of The Table Data')
        print(f'List of the table {data}')
        return data

    def selected_random_keyword(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            if 1 < len(item.text.splitlines()):
                data.append(item.text.splitlines())
        key = data[random.randint(0, len(data) - 1)][random.randint(0, 5)]
        print(f'The choice of a random keyword for finding a line in a table containing it: {key}')
        return key

    def search_some_person(self, key_word):
        print('Start search')
        self.element_is_visible(self.locators.INPUT_SEARCH).clear()
        self.element_is_visible(self.locators.INPUT_SEARCH) and \
        self.element_is_visible(self.locators.INPUT_SEARCH).send_keys(key_word)
        print(f'Entering the keyword <{key_word}> in the search field')

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.ALL_DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        print(f'Find the line containing the keyword: {row.text.splitlines()}')
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(self.locators.EDIT_BUTTONS).click()
        print('Click Edit Button')
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).clear()
        print('Clear Field First Name')
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        print(f'Input Value First Name <{first_name}>')
        self.element_is_visible(self.locators.EMAIL_INPUT).clear()
        print('Clear Field Email')
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        print(f'Input Value Email <{email}>')
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        print('Clear Field Age')
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        print(f'Input Value Age <{age}>')
        self.element_is_visible(self.locators.SALARY_INPUT).clear()
        print('Clear Field Salary')
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
        print(f'Input Value Salary <{salary}>')
        self.element_is_visible(self.locators.DEPARTAMENT_INPUT).clear()
        print('Clear Field Department')
        self.element_is_visible(self.locators.DEPARTAMENT_INPUT).send_keys(department)
        print(f'Input Value Department <{department}>')
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        print('Click Submit')
        return first_name, str(age), email, str(salary), department

    def clear_registration_form(self):
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).clear()
        self.element_is_visible(self.locators.LAST_NAME_INPUT).clear()
        self.element_is_visible(self.locators.EMAIL_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.SALARY_INPUT).clear()
        self.element_is_visible(self.locators.DEPARTAMENT_INPUT).clear()

    def before_update_person_info(self):
        self.get_edit_button()
        list_lines = self.element_is_visible(self.locators.REGISTRATION_FORM_ALL_LINES)
        print(list_lines.text)
        # data = []
        # for item in list_lines:
        #     data.append(item.value.text.splitlines())
        # print(data)
        return list_lines.text  # data

    def after_update_person_info(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        print(f'After update name {first_name}')
        last_name = person_info.last_name
        print(f'After update last name {last_name}')
        email = person_info.email
        print(f'After update email {email}')
        age = person_info.age
        print(f'After update age {age}')
        salary = person_info.salary
        print(f'After update salary {salary}')
        department = person_info.department
        print(f'After update department {department}')
        edit_person = f'{first_name, last_name, email, age, salary, department}'
        self.element_is_visible(self.locators.EDIT_BUTTONS).click()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(edit_person[0])
        print(f'Input first name is: {first_name}')
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(edit_person[1])
        print(f'Input first name is: {last_name}')
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(edit_person[2])
        print(f'Input first name is: {email}')
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(edit_person[3])
        print(f'Input first name is: {age}')
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(edit_person[4])
        print(f'Input first name is: {salary}')
        self.element_is_visible(self.locators.DEPARTAMENT_INPUT).send_keys(edit_person[5])
        print(f'Input first name is: {department}')
        return edit_person

    def get_edit_button(self):
        print('click edit button')
        self.element_is_visible(self.locators.EDIT_BUTTONS).click()

    def delete_person(self, name):
        self.element_is_visible(self.locators.ALL_DELETE_BUTTON) and \
        self.elements_is_clickable(self.locators.ALL_DELETE_BUTTON).click()
        print(f'Delete Person {name}')

    def check_deleted(self):
        return self.element_is_visible(self.locators.NO_ROW).text

    def change_the_number_of_line(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.SELECT_NUMBER_ROWS)
            self.go_to_element(count_row_button)
            print(f'Select {x}')
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
            print(f'Count rows is :{self.check_count_rows()}')
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    # Methods

    def web_table_add_new_person_and_check_this(self):
        Logger.add_start_step(method='web_table_add_new_person_and_check_this')
        new_person = self.add_new_person()
        table_person = self.check_added_new_person()
        print('Compare whether the created data appeared in the table')
        assert f'{new_person}' in f'{table_person}', 'Created data is not in the table'
        Logger.add_end_step(url=self.driver.current_url, method='web_table_add_new_person_and_check_this')

    def web_table_search_added_person(self):
        Logger.add_start_step(method='web_table_search_added_person')
        self.add_new_person()
        self.check_added_new_person()
        random_key_word = self.selected_random_keyword()
        self.search_some_person(f'{random_key_word}')
        table_result = self.check_search_person()
        print(f'Random key word: {random_key_word}')
        print(f'Table result: {table_result}')
        assert f'{random_key_word}' in f'{table_result}', 'The Person Was Not Found In The Table'
        Logger.add_end_step(url=self.driver.current_url, method='web_table_search_added_person')

    def web_table_update_person_info(self):
        Logger.add_start_step(method='web_table_update_person_info')
        self.remove_fixedban()
        last_name = self.add_new_person()[1]
        self.search_some_person(last_name)
        edit_person_data = self.update_person_info()
        row = self.check_search_person()
        for edit_person_data in str(row):
            assert str(edit_person_data) in str(row), f'Updated element {edit_person_data} not in the table'
        Logger.add_end_step(url=self.driver.current_url, method='web_table_update_person_info')

    def remove_person_from_web_table_and_check_this(self):
        Logger.add_start_step(method='remove_person_from_web_table_and_check_this')
        self.remove_fixedban()
        email = self.add_new_person()[3]
        self.search_some_person(email)
        self.delete_person(f'{email}')
        text = self.check_deleted()
        print(f'Checked deleted by email {email}')
        assert text == 'No rows found', f'{email} Person have not deleted'
        Logger.add_end_step(url=self.driver.current_url, method='remove_person_from_web_table_and_check_this')

    def change_the_number_of_rows_and_count_them(self):
        Logger.add_start_step(method='change_the_number_of_rows_and_count_them')
        self.remove_fixedban()
        self.remove_footer()
        count = self.change_the_number_of_line()
        assert count == [5, 10, 20, 25, 50, 100], 'Selected number of rows is not equal to those presented'
        Logger.add_end_step(url=self.driver.current_url, method='change_the_number_of_rows_and_count_them')


class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    # Actions

    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK))
        print('Double Clicked')
        return self.check_result_click(self.locators.DOUBLE_CLICK)

    def right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK))
        print('Right Clicked')
        return self.check_result_click(self.locators.RIGHT_CLICK)

    def click_me(self):
        self.action_one_click(self.element_is_visible(self.locators.CLICK_ME))
        print('Click Me Clicked')
        return self.check_result_click(self.locators.CLICK_ME)

    def check_result_click(self, output):
        print('Output Message: ', self.element_is_present(output).text)
        return self.element_is_present(output).text

    # Method
    def different_click_on_the_buttons(self):
        Logger.add_start_step(method='different_click_on_the_buttons')
        self.remove_footer()
        self.remove_fixedban()
        self.double_click()
        self.right_click()
        self.click_me()
        Logger.add_end_step(url=self.driver.current_url, method='different_click_on_the_buttons')
