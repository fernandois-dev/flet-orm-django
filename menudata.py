import flet as ft


class ControlGroup:
    def __init__(self, name: str, label: str, icon: str, selected_icon: str = None, children: list = None):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon or icon
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)


class MenuData:
    def __init__(self):
        self.control_groups = self.get_control_groups()

    def get_control_groups(self):
        return [
            ControlGroup(
                name="",
                label="Home",
                icon=ft.icons.HOME,
                selected_icon=ft.icons.HOME_OUTLINED,
            ),
            ControlGroup(
                name="product",
                label="Product",
                icon=ft.icons.SHOPPING_BAG_OUTLINED,
                selected_icon=ft.icons.SHOPPING_BAG,
            ),
        ]

