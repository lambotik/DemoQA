from pages.Interactions.interactions_page import SortablePage, SelectablePage, ResizablePage, DragAndDropPage, \
    DragabblePage


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

    class TestResizable:
        def test_check_change_size_resizable_windows(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size, min_size = resizable_page.change_resizable_box()
            size_before, size_after = resizable_page.change_resizable()
            assert max_size == 'width: 500px; height: 300px;', 'Maximum size not equal width: 500px; height: 300px;'
            assert min_size == 'width: 150px; height: 150px;', 'Minimum size not equal width: 150px; height: 150px;'
            assert size_before != size_after, 'Resizable has not been changed'

    class TestDragAndDrop:
        def test_check_drag_and_drop_simple(self, driver):
            drag_and_drop_page = DragAndDropPage(driver, 'https://demoqa.com/droppable')
            drag_and_drop_page.open()
            text = drag_and_drop_page.drop_simple()
            assert text == 'Dropped!', 'The element has not been dropped'

        def test_check_drag_and_drop_acceptable(self, driver):
            drag_and_drop_page = DragAndDropPage(driver, 'https://demoqa.com/droppable')
            drag_and_drop_page.open()
            accept, not_accept = drag_and_drop_page.drop_accept()
            assert accept == 'Dropped!', 'The element has not been accepted'
            assert not_accept == 'Drop here', 'The element has been accepted'

        def test_check_drop_prevent_propogation(self, driver):
            drag_and_drop_page = DragAndDropPage(driver, 'https://demoqa.com/droppable')
            drag_and_drop_page.open()
            not_greedy_box, not_greedy, greedy_box, greedy = drag_and_drop_page.drop_prevent_propogation()
            assert not_greedy_box == 'Dropped!', 'The elements text has not been changed'
            assert not_greedy == 'Dropped!', 'The elements text has not been changed'
            assert greedy_box == 'Outer droppable', 'The elements text has been changed'
            assert greedy == 'Dropped!', 'The element text has not been changed'

        def test_check_drop_will_revert(self, driver):
            drag_and_drop_page = DragAndDropPage(driver, 'https://demoqa.com/droppable')
            drag_and_drop_page.open()
            position_before, position_after, text = drag_and_drop_page.drop_will_revert()
            assert position_before == position_after, 'The element has not been revert'
            assert text == 'Dropped!', 'The element text has not been changed'

        def test_check_drop_will_not_revert(self, driver):
            drag_and_drop_page = DragAndDropPage(driver, 'https://demoqa.com/droppable')
            drag_and_drop_page.open()
            position_before, position_after, text = drag_and_drop_page.drop_will_not_revert()
            assert position_before != position_after, 'The element has not been revert'
            assert text == 'Dropped!', 'The element text has not been changed'

    class TestDragabble:
        def test_sample_drag_box(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            position_before, position_after = dragabble_page.sample_drag_box()
            assert position_before != position_after, 'The position of the box has not been changed'

        def test_axis_restricted_x(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            left_px_before, top_px_before, left_px_after, top_px_after = dragabble_page.axis_restricted_x()
            assert left_px_before != left_px_after and top_px_before == top_px_after, \
                'The position of the box has not changed or it has shifted off the axis'

        def test_axis_restricted_y(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            left_px_before, top_px_before, left_px_after, top_px_after = dragabble_page.axis_restricted_y()
            assert left_px_before == left_px_after and top_px_before != top_px_after, \
                'The position of the box has not changed or it has shifted off the axis'
