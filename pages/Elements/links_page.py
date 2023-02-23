import requests

from locators.elements_page_locators import LinksPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class LinksPage(BasePage):
    locators = LinksPageLocators()

    # Getters

    def get_created_link(self):
        return self.element_is_visible(self.locators.CREATED_LINK)

    def get_bad_request(self):
        return self.element_is_visible(self.locators.BAD_REQUEST_LINK)

    def get_no_content_link(self):
        return self.element_is_visible(self.locators.NO_CONTENT_LINK)

    def get_moved_link(self):
        return self.element_is_visible(self.locators.MOVED_LINK)

    def get_unauthorized_link(self):
        return self.element_is_visible(self.locators.UNAUTHORIZED_LINK)

    def get_forbidden_link(self):
        return self.element_is_visible(self.locators.FORBIDDEN_LINK)

    def get_not_found_link(self):
        return self.element_is_visible(self.locators.NOT_FOUND_LINK)

    # Actions

    def click_created_link(self):
        print('Click created link')
        self.get_created_link().click()

    def click_bad_request(self):
        print('Click bad request link')
        self.get_bad_request().click()

    def click_no_content_link(self):
        print('Click no content link')
        self.get_no_content_link().click()

    def click_moved_link(self):
        print('Click moved link')
        self.get_moved_link().click()

    def click_unauthorized_link(self):
        print('Click unauthorized link')
        self.get_unauthorized_link().click()

    def click_forbidden_link(self):
        print('Click forbidden link')
        self.get_forbidden_link().click()

    def click_not_found_link(self):
        print('Click not found link')
        self.get_not_found_link().click()

    def link_response_code_200(self):
        home_link = self.element_is_present(self.locators.HOME_LINK)
        home_link_href = home_link.get_attribute('href')
        home_link_status_code = requests.get(home_link_href).status_code
        if home_link_status_code == 200:
            print('Click on home link')
            home_link.click()
            print('Go to a new tab')
            self.go_to_a_new_tab()
            url = self.driver.current_url
            print(f'Link href: {home_link_href}\nUrl: {url}\nUrl status code: {home_link_status_code}')
            return home_link_href, url, home_link_status_code
        else:
            request = requests.get(f'{home_link_href}')
            home_link_status_code = request.status_code
            home_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            print(f'Link href: {home_link_href}\nUrl: {url}\nUrl status code: {home_link_status_code}')
            return home_link_href, url, home_link_status_code

    def assert_link_response_code_200(self):
        href_link, current_link, status_code = self.link_response_code_200()
        assert href_link == current_link, f'Bad link url {status_code}'

    def assert_response_code(self, status_code):
        link_response_code = self.element_is_present(self.locators.LINK_RESPONSE_CODE).text
        print(f'Result status code: {link_response_code}')
        print('Assertion, link status code, and result')
        assert status_code == link_response_code, f'Status code is {status_code}'

    """"Добавляет к пути основной ссылки отправляемый запрос и возвращает статус код,
     в скобках нужно вставить локатор"""

    def get_link_and_check_code_status(self, request):
        self.element_is_present(request)
        home_link = self.element_is_present(self.locators.HOME_LINK)
        home_link_href = home_link.get_attribute('href')
        print('Home link URL: ', home_link_href)
        id_text = self.element_is_present(request).get_attribute("id")  # Получает значение id
        current_url = self.driver.current_url
        bad_url = home_link_href + id_text
        print('Adding the path ending to the home page:', bad_url)
        print('Sent a request to the received URL')
        status_code = requests.get(f'{bad_url}').status_code
        print('Gotten status code is: ', status_code)
        return status_code

    # Methods

    def check_link_response_code_200(self):
        Logger.add_start_step(method='check_link_response_code_200')
        self.assert_link_response_code_200()
        Logger.add_end_step(url=self.driver.current_url, method='check_link_response_code_200')

    def check_link_bad_response(self):
        Logger.add_start_step(method='check_bad_request')
        response = self.get_link_and_check_code_status(self.locators.BAD_REQUEST_LINK)
        self.click_bad_request()
        self.assert_response_code(f'{response}')
        Logger.add_end_step(url=self.driver.current_url, method='check_bad_request')

    def check_link_created_response(self):
        Logger.add_start_step(method='check_link_created_request')
        response = self.get_link_and_check_code_status(self.locators.CREATED_LINK)
        self.click_created_link()
        self.assert_response_code(f'{response}')
        Logger.add_end_step(url=self.driver.current_url, method='check_link_created_request')

    def check_link_no_content_response(self):
        Logger.add_start_step(method='check_link_no_content_response')
        response = self.get_link_and_check_code_status(self.locators.NO_CONTENT_LINK)
        self.click_no_content_link()
        self.assert_response_code(f'{response}')
        Logger.add_end_step(url=self.driver.current_url, method='check_link_no_content_response')

    def check_link_moved_response(self):
        Logger.add_start_step(method='check_link_moved_response')
        response = self.get_link_and_check_code_status(self.locators.MOVED_LINK)
        self.click_moved_link()
        self.assert_response_code(f'{response}')
        Logger.add_end_step(url=self.driver.current_url, method='check_link_moved_response')

    def check_link_unauthorized_response(self):
        Logger.add_start_step(method='check_link_unauthorized_response')
        response = self.get_link_and_check_code_status(self.locators.UNAUTHORIZED_LINK)
        self.click_unauthorized_link()
        self.assert_response_code(f'{response}')
        Logger.add_end_step(url=self.driver.current_url, method='check_link_unauthorized_response')

    def check_link_forbidden_response(self):
        Logger.add_start_step(method='check_link_forbidden_response')
        response = self.get_link_and_check_code_status(self.locators.FORBIDDEN_LINK)
        self.click_forbidden_link()
        self.assert_response_code(f'{response}')
        Logger.add_end_step(url=self.driver.current_url, method='check_link_forbidden_response')

    def check_link_not_found_response(self):
        Logger.add_start_step(method='check_link_not_found_response')
        response = self.get_link_and_check_code_status(self.locators.NOT_FOUND_LINK)
        self.go_to_element(self.element_is_present(self.locators.NOT_FOUND_LINK))
        self.click_not_found_link()
        self.assert_response_code(f'{response}')
        Logger.add_end_step(url=self.driver.current_url, method='check_link_not_found_response')
