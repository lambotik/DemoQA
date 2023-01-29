from selenium.webdriver.common.by import By


class AccordianPageLocators:
    # Accordian
    FIRST_TAB = (By.XPATH, '//div[@id="section1Heading"]')
    FIRST_TAB_TEXT = (By.XPATH, '//div[@id="section1Content"]/p')
    SECOND_TAB = (By.XPATH, '//div[@id="section2Heading"]')
    SECOND_TAB_TEXT = (By.XPATH, '//div[@id="section2Content"]/p')
    THIRD_TAB = (By.XPATH, '//div[@id="section3Heading"]')
    THIRD_TAB_TEXT = (By.XPATH, '//div[@id="section3Content"]/p')


class AutoCompletePageLocators:
    # Auto complete
    INPUT_MULTI = (By.XPATH, '//input[@id="autoCompleteMultipleInput"]')
    LIST_MULTI_VALUE = (By.XPATH, '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    CLOSE_MULTI_VALUE_ELEMENT = (
        By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    INPUT_SINGLE = (By.XPATH, '//input[@id="autoCompleteSingleInput"]')
    SINGLE_CONTAINER = (By.XPATH, '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    SLIDER_VALUE = (By.XPATH, '//input[@id="sliderValue"]')
    INPUT_SLIDER = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')


class ProgressBarPageLocators:
    START_AND_STOP_BUTTON = (By.XPATH, '//button[@id="startStopButton"]')
    PROGRESS_BAR = (By.XPATH, '//div[@id="progressBar"]')


class TabsPageLocators:
    TAB_WHAT = (By.XPATH, '//a[@id="demo-tab-what"]')
    TAB_WHAT_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]')
    TAB_ORIGIN = (By.XPATH, '//a[@id="demo-tab-origin"]')
    TAB_ORIGIN_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-origin"]')
    TAB_USE = (By.XPATH, '//a[@id="demo-tab-use"]')
    TAB_USE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-use"]')
    TAB_MORE = (By.XPATH, '//a[@id="demo-tab-more"]')
    TAB_CONTENT = (By.XPATH, '//div[@class="tab-content"]')
