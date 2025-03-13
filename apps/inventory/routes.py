from .views import product_list, product_form

routes = {
    '/product': product_list,
    '/product/form': product_form,
}
