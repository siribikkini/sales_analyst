from django.contrib import admin
from django.urls import path

from saapp1.views import (
    home,
    products_view,
    add_product,
    add_customer,
    customers_view,
    admin_page,
    orders_view,
    add_order,
    orderitems,
    # orderitems_view
    delete_orderitem,
    analytics,
    delete_customer,
    delete_order,
    delete_product
)


urlpatterns = [

    # Django built-in admin
    path('admin/', admin.site.urls),

    # Home
    path('home/', home, name='home'),

    # Products
    path('products/', products_view, name='products'),
    path('add-product/', add_product, name='add_product'),

    # Customers
    path('customers/', customers_view, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),

    # Custom Admin Dashboard
    path('my-admin/', admin_page, name='my_admin'),

    # Orders
    path('orders/', orders_view, name='orders'),
    path('add-order/', add_order, name='add_order'),

    path('orderitems/',orderitems,name="order_items"),
    # path('orderitems-view',orderitems_view,name="orderitems_view")
    path(
    'delete-orderitem/<int:id>/',
    delete_orderitem,name='delete_orderitem'
),
path("analytics/",analytics,name="analytic_page"),
path('delete-customer/<int:id>/', delete_customer, name='delete_customer'),
path('delete-order/<int:id>/', delete_order, name='delete_order'),
path('delete-product/<int:id>/', delete_product, name='delete_product')]