from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    LIST_ITEMS_LIST_TAB = (
    By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    LIST_ITEMS_GRID_TAB = (
    By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')
