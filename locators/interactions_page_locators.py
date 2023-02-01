from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    LIST_ITEMS_LIST_TAB = (
        By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    LIST_ITEMS_GRID_TAB = (
        By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    LIST_ITEMS_LIST_TAB = (
        By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ACTIVE_ITEMS_LIST_TAB = (
        By.CSS_SELECTOR,
        'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')
    LIST_ITEMS_GRID_TAB = (
        By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item list-group-item-action"]')
    LIST_ACTIVE_ITEMS_GRID_TAB = (
        By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item active list-group-item-action"]')
