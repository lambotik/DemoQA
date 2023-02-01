from pages.Interactions.interactions_page import SortablePage, SelectablePage


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

    class TestSelectable:
        def test_check_change_list_order(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selected_items, unselected_items = selectable_page.random_selection_and_return_active_and_inactive_elements()
            assert unselected_items not in selected_items, 'Elements are selected and canceled'

        def test_check_change_grid_order(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selected_items, unselected_items = selectable_page.grid_random_selection_and_return_active_and_inactive_elements()
            assert unselected_items not in selected_items, 'Elements are selected and canceled'
