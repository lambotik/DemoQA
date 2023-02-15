import random
import re
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DragAndDropPageLocators, DragabblePageLocators
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
        str_active = ' '.join(list_active_elements)
        str_inactive = ' '.join(list_not_selected_elements)
        Logger.add_end_step(url=self.driver.current_url,
                            method='random_selection_and_return_active_and_inactive_elements')
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

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size
        return width

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        value_size = size.get_attribute('style')
        return value_size

    def change_resizable_box(self):
        Logger.add_start_step(method='change_resizable_box')
        value_before = self.get_max_min_size(self.locators.RESIZABLE_BOX)
        print(f'Starting size, resizable box: {value_before}')
        self.action_drag_and_drop_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        print(f'Resizable box max size: {max_size}')
        self.action_drag_and_drop_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        print(f'Resizable box min size: {min_size}')
        Logger.add_end_step(url=self.driver.current_url, method='change_resizable_box')
        return max_size, min_size

    def change_resizable(self):
        Logger.add_start_step(method='change_resizable')
        self.element_is_visible(self.locators.RESIZABLE)
        value_before = self.get_max_min_size(self.locators.RESIZABLE)
        print(f'Starting size, resizable tab: {value_before}')
        self.action_drag_and_drop_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                         random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        print(f'Resizable tab max size: {max_size}')
        self.action_drag_and_drop_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                         random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        print(f'Resizable tab min size: {min_size}')
        Logger.add_end_step(url=self.driver.current_url, method='change_resizable')
        return max_size, min_size


class DragAndDropPage(BasePage):
    locators = DragAndDropPageLocators()

    def drop_simple(self):
        Logger.add_start_step(method='drop_simple')
        self.element_is_visible(self.locators.SIMPLE).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        drop_div = self.element_is_visible(self.locators.DROPPABLE)
        self.action_drag_and_drop_element(drag_div, drop_div)
        print(drop_div.text)
        Logger.add_end_step(url=self.driver.current_url, method='drop_simple')
        return drop_div.text

    def drop_accept(self):
        Logger.add_start_step(method='drop_accept')
        self.element_is_visible(self.locators.ACCEPT).click()
        acceptable = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE)
        self.action_drag_and_drop_element(not_acceptable, drop_div)
        drop_div_not_accept = drop_div.text
        print(drop_div_not_accept)
        self.action_drag_and_drop_element(acceptable, drop_div)
        drop_div_accept = drop_div.text
        print(drop_div_accept)
        Logger.add_end_step(url=self.driver.current_url, method='drop_accept')
        return drop_div_accept, drop_div_not_accept

    def drop_prevent_propogation(self):
        Logger.add_start_step(method='drop_prevent_propogation')
        self.element_is_visible(self.locators.PREVENT_PROPOGATION).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_BOX)
        not_greedy = self.element_is_visible(self.locators.NOT_GREEDY)
        greedy_box = self.element_is_visible(self.locators.GREEDY_BOX)
        greedy = self.element_is_visible(self.locators.GREEDY)
        self.action_drag_and_drop_element(drag_div, not_greedy)
        not_greedy_box_text = not_greedy_box.text
        not_greedy_text = not_greedy.text
        self.action_drag_and_drop_element(drag_div, greedy)
        greedy_box_text = greedy_box.text
        greedy_text = greedy.text
        Logger.add_end_step(url=self.driver.current_url, method='drop_prevent_propogation')
        return not_greedy_box_text, not_greedy_text, greedy_box_text, greedy_text

    def drop_will_revert(self):
        Logger.add_start_step(method='drop_will_revert')
        self.element_is_visible(self.locators.REVERT_DRAGGABLE).click()
        drag_div = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.REVERT_DROP_HERE)
        self.action_drag_and_drop_offset(self.element_is_visible(self.locators.WILL_REVERT), 0, 1)
        drag_div_position_before = drag_div.get_attribute('style')
        self.action_drag_and_drop_element(drag_div, drop_div)
        time.sleep(1)
        drag_div_position_after = drag_div.get_attribute('style')
        Logger.add_end_step(url=self.driver.current_url, method='drop_will_revert')
        return drag_div_position_before, drag_div_position_after, drop_div.text

    def drop_will_not_revert(self):
        Logger.add_start_step(method='drop_will_not_revert')
        self.element_is_visible(self.locators.REVERT_DRAGGABLE).click()
        drag_div = self.element_is_visible(self.locators.NOT_REVERT)
        drop_div = self.element_is_visible(self.locators.REVERT_DROP_HERE)
        self.action_drag_and_drop_offset(self.element_is_visible(self.locators.NOT_REVERT), 0, 1)
        time.sleep(1)
        drag_div_position_before = drag_div.get_attribute('style')
        self.action_drag_and_drop_element(drag_div, drop_div)
        time.sleep(1)
        drag_div_position_after = drag_div.get_attribute('style')
        Logger.add_end_step(url=self.driver.current_url, method='drop_will_not_revert')
        return drag_div_position_before, drag_div_position_after, drop_div.text


class DragabblePage(BasePage):
    locators = DragabblePageLocators()

    def get_element_position_before_after(self, element):
        self.action_drag_and_drop_offset(element, random.randint(0, 50), random.randint(0, 50))
        position_before = element.get_attribute('style')
        self.action_drag_and_drop_offset(element, random.randint(0, 50), random.randint(0, 50))
        position_after = element.get_attribute('style')
        return [position_before], [position_after]

    def sample_drag_box(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        position_before, position_after = self.get_element_position_before_after(drag_div)
        print(f'Position element before: {position_before}')
        print(f'Position element after: {position_after}')
        return position_before, position_after

    def get_position(self, position):
        position_before = position[0]
        left = position_before[0]
        top = position_before[0]
        l = re.findall(r'\d+', left)
        t = re.findall(r'\d+', top)
        le = [int(i) for i in l][0]
        to = [int(i) for i in t][1]
        print('value left:', le)
        print('value top', to)
        position_a = position[1]
        left_after = position_a[0]
        top_after = position_a[0]
        l = re.findall(r'\d+', left_after)
        t = re.findall(r'\d+', top_after)
        le_a = [int(i) for i in l][0]
        to_a = [int(i) for i in t][1]
        print('value left after:', le_a)
        print('value top after', to_a)
        return le, to, le_a, to_a

    def axis_restricted_x(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED).click()
        only_x = self.element_is_visible(self.locators.ONLY_X)
        position = self.get_element_position_before_after(only_x)
        print(position)
        left_b, top_b, left_a, top_a = self.get_position(position)
        return left_b, top_b, left_a, top_a

    def axis_restricted_y(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED).click()
        only_y = self.element_is_visible(self.locators.ONLY_Y)
        position = self.get_element_position_before_after(only_y)
        print(position)
        left_b, top_b, left_a, top_a = self.get_position(position)
        return left_b, top_b, left_a, top_a
