import flet as ft

class HomePage(ft.Container):
    def __init__(self, page: ft.Page, params = {}):
        super().__init__()
        self.content =  ft.Text("HOME", size=30)
