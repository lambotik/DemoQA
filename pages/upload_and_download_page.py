import base64
import os
import random

from generator.generator import generated_file
from locators.elements_page_locators import UploadAndDownloadPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    # Actions

    def upload_file(self):
        file_name, path = generated_file()
        print(f'Generated file name is: {file_name}')
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        file = file_name.split('\\')[-1]
        print(f'Uploaded file is: {file}')
        name_uploaded_file = self.element_is_present(self.locators.RESULT_UPLOADED_BUTTON).text
        name_uploaded_file = name_uploaded_file.split('\\')[-1]
        print('Get name uploaded file')
        print(f'Uploaded file name is: {name_uploaded_file}')
        print(f'Remove {file}')
        os.remove(path)
        return file, name_uploaded_file

    def download_file(self):
        # получаем закодированную ссылку загружаемого файла
        link = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
        print(f'Get encoded link href: {link}')
        # декодируем ссылку в байты
        link_b = base64.b64decode(link)
        print('Decode the link into bytes')
        # прописываем путь для сохранения получаемой картинки
        path_name_file = rf'C:\Users\Дима\PycharmProjects\DemoQA\FileTestjpg{random.randint(0, 999)}.jpg'
        file_name = path_name_file.split('\\')[-1]
        with open(path_name_file, 'wb+') as f:
            ''' отсекаем от декодированного кода лишние значения до искомого \xff\xd8,
            (после этого значения хранится интересующая нас информация)'''
            offset = link_b.find(b'\xff\xd8')
            print('We cut off unnecessary values from the decoded code to the desired one')
            # записываем очищенную нужную информацию в файл jpg
            f.write(link_b[offset:])
            # проверяем что path_name_file есть в пути, получаем True
            check_file = os.path.exists(path_name_file)
            print(f'Checking that the downloaded file <{file_name}> in the {path_name_file}')
            f.close()
        os.remove(path_name_file)
        print(f'Remove {file_name}')
        return check_file

    # Methods

    def file_upload_check(self):
        Logger.add_start_step(method='file_upload_check')
        self.upload_file()
        Logger.add_end_step(url=self.driver.current_url, method='file_upload_check')

    def download_file_check(self):
        Logger.add_start_step(method='download_file_check')
        check = self.download_file()
        assert check is True, 'The file has not been downloaded'
        Logger.add_end_step(url=self.driver.current_url, method='download_file_check')
