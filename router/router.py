# in a new file, e.g., router.py
import flet as ft
from pages.home_page import HomePage
from utilities.template_routes import TemplateRoute
from pages.not_found_page import NotFoundPage
from apps.inventory.routes import routes as inventory_routes




class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        defaults_routes = {
            '/': lambda page, params : HomePage(page=page, params=params)
        }
        self.routes = defaults_routes | inventory_routes
        

    def get_page(self, route: str, params: dict = {}) -> ft.Control | None:
        troute = TemplateRoute(route, params=params)
        
        for pattern, factory in self.routes.items():
            if troute.match(pattern):
                try:
                    return factory(self.page, troute.params)
                except Exception as e:
                    # Log the error, maybe display a generic error page
                    print(f"Error instantiating page for route {route}: {e}")
                    # return ErrorPage()
                    return None

        return NotFoundPage() 
