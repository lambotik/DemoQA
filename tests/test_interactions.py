import pytest

from pages.Interactions.interactions_page import SortablePage


class TestInteractionsPage:
    class TestSortable:
        def test_check_change_list_order(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after, 'The order of thr list has not been changed'

        def test_check_change_grid_order(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after, 'The order of thr list has not been changed'

