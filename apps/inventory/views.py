from pages.generic_page import GenericPage
from apps.inventory.models import Product
import flet as ft

from pages.generic_page_form_standard import GenericPageFormStandar



def product_list(page: ft.Page, params: dict):
    view = GenericPage(page=page, _model=Product, params=params)
    view.build_page()
    return view
    

def product_form(page: ft.Page, params: dict):
    view = GenericPageFormStandar(page=page, _model=Product, params=params)
    return view

