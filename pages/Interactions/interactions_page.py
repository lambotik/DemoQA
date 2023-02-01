import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
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


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def get_list_elements(self, elements):
        item_list = self.elements_are_visible(elements)
        data = []
        for item in item_list:
            data.append(item)
        return data

    def random_selection_and_return_active_and_inactive_elements(self):
        Logger.add_start_step(method='random_selection_and_return_active_and_inactive_elements')
        self.element_is_visible(self.locators.LIST).click()
        list_elements = self.get_list_elements(self.locators.LIST_ITEMS_LIST_TAB)
        for i in range(len(list_elements) - 1):
            random.choice(list_elements).click()
        active_element = self.elements_are_visible(self.locators.LIST_ACTIVE_ITEMS_LIST_TAB)
        list_active_elements = [item.text for item in active_element]
        print('List of active elements', list_active_elements)
        not_selected_elements = self.get_list_elements(self.locators.LIST_ITEMS_LIST_TAB)
        list_not_selected_elements = [item.text for item in not_selected_elements]
        print('List of inactive elements: ', list_not_selected_elements)
        Logger.add_end_step(url=self.driver.current_url,
                            method='random_selection_and_return_active_and_inactive_elements')
        str_active = ' '.join(list_active_elements)
        str_inactive = ' '.join(list_not_selected_elements)
        return str_active, str_inactive

    def grid_random_selection_and_return_active_and_inactive_elements(self):
        Logger.add_start_step(method='grid_random_selection_and_return_active_and_inactive_elements')
        self.element_is_visible(self.locators.GRID).click()
        list_elements = self.get_list_elements(self.locators.LIST_ITEMS_GRID_TAB)
        for i in range(len(list_elements) - 1):
            random.choice(list_elements).click()
        active_element = self.elements_are_visible(self.locators.LIST_ACTIVE_ITEMS_GRID_TAB)
        list_active_elements = [item.text for item in active_element]
        print('List of active elements', list_active_elements)
        not_selected_elements = self.get_list_elements(self.locators.LIST_ITEMS_GRID_TAB)
        list_not_selected_elements = [item.text for item in not_selected_elements]
        print('List of inactive elements: ', list_not_selected_elements)
        str_active = ' '.join(list_active_elements)
        str_inactive = ' '.join(list_not_selected_elements)
        Logger.add_end_step(url=self.driver.current_url,
                            method='grid_random_selection_and_return_active_and_inactive_elements')
        return str_active, str_inactive



class ResizablePage(BasePage):
    locators = ResizablePageLocators()
