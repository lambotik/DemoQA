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


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR,
                            'div[id="resizableBoxWithRestriction"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')
    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')


class DragAndDropPageLocators:
    # Simple
    SIMPLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROPPABLE = (By.CSS_SELECTOR, 'div[id="droppableExample-tabpane-simple"] div[id="droppable"]')
    # Accept
    ACCEPT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE = (By.CSS_SELECTOR, 'div[id="droppableExample-tabpane-accept"] div[id="droppable"]')
    # Prevent Propogation
    PREVENT_PROPOGATION = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    NOT_GREEDY_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    # Revert Draggable
    REVERT_DRAGGABLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    REVERT_DROP_HERE = (By.CSS_SELECTOR, 'div[id="droppableExample-tabpane-revertable"] div[id="droppable"]')

class DragabblePageLocators:
    # Simple
    SIMPLE = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"]')

    # Axis Restricted
    AXIS_RESTRICTED = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')