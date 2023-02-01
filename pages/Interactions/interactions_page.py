import random

from locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        Logger.add_start_step(method='change_list_order')
        self.element_is_visible(self.locators.LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEMS_LIST_TAB)
        print(order_before)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEMS_LIST_TAB), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEMS_LIST_TAB)
        print(order_after)
        Logger.add_end_step(url=self.driver.current_url, method='change_list_order')
        return order_before, order_after

    def change_grid_order(self):
        Logger.add_start_step(method='change_grid_order')
        self.element_is_visible(self.locators.GRID).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEMS_GRID_TAB)
        print(order_before)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEMS_GRID_TAB), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEMS_GRID_TAB)
        print(order_after)
        Logger.add_end_step(url=self.driver.current_url, method='change_grid_order')
        return order_before, order_after
