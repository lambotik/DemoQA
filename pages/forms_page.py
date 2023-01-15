import os
import random

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_subject, generated_file
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class FormsPage(BasePage):
    locators = FormsPageLocators()

    def fill_all_fields(self):
        Logger.add_start_step(method='fill_all_fields')
        self.remove_footer()
        self.remove_fixedban()
        person = next(generated_person())
        first_name = person.first_name
        last_name = person.last_name
        email = person.email
        phone = random.randint(1000000000, 9999999999)
        current_address = person.current_address
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).send_keys(f'{first_name}')
        print(f'Input First Name: {first_name}')
        self.element_is_visible(self.locators.INPUT_LAST_NAME).send_keys(f'{last_name}')
        print(f'Input Last Name: {last_name}')
        self.element_is_visible(self.locators.INPUT_USER_EMAIL).send_keys(f'{email}')
        print(f'Input Email: {email}')
        gender = self.element_is_visible(self.locators.SELECT_GENDER).click()
        # print(f'Select Gender: {gender}')
        self.element_is_visible(self.locators.INPUT_MOBILE_NUBER).send_keys(phone)
        print(f'Input Phone: {phone}')
        date_of_birth = self.element_is_visible(self.locators.INPUT_DATE_OF_BIRTH).get_attribute('value')
        print(f'Date of birth: {date_of_birth}')
        self.element_is_visible(self.locators.INPUT_SUBJECTS).click()
        subject = self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(generated_subject())
        self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(Keys.RETURN)
        hobbies = self.element_is_visible(self.locators.INPUT_HOBBIES).click()
        # print(f'Select Hobbies: {hobbies}')
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(path)
        print(f'Uploaded file name: {file_name}\nPath: {path}')
        self.element_is_visible(self.locators.INPUT_CURRENT_ADDRESS).send_keys(current_address)
        print(f'Current Address: {current_address}')
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(Keys.RETURN)
        select_city = self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.INPUT_CITY).send_keys(Keys.RETURN)
        state = self.element_is_visible(self.locators.STATE_TEXT).text
        print(f'State: {state}')
        city = self.element_is_visible(self.locators.CITY_TEXT).text
        print(f'City: {city}')
        self.element_is_visible(self.locators.SUBMIT).click()
        print('Click Submit')
        os.remove(path)
        Logger.add_end_step(url=self.driver.current_url, method='fill_all_fields')
        return str(first_name), str(last_name), str(email), str(phone), str(date_of_birth), str(path), \
            str(current_address), str(state), str(city)

    def form_result(self):
        Logger.add_start_step(method='form_result')
        result_list = self.elements_are_present(self.locators.TABLE_RESULT)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        Logger.add_end_step(url=self.driver.current_url, method='form_result')
        return data
