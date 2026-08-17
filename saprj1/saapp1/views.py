from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Customer, Order, OrderItem


# Home page
def home(request):
    return render(request, 'home.html')


# Custom admin page
def admin_page(request):
    return render(request, 'admin.html')


# ---------------- PRODUCTS ----------------

# Display all products
def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# Add a product
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        price = request.POST['price']
        stock = request.POST['stock']

        Product.objects.create(
            name=name,
            category=category,
            price=price,
            stock=stock
        )

        return redirect('products')

    return render(request, 'add_product.html')


# ---------------- CUSTOMERS ----------------

# Display all customers
def customers_view(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})


# Add a customer
def add_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        Customer.objects.create(
            name=name,
            email=email,
            phone=phone
        )

        return redirect('customers')

    return render(request, 'add_customer.html')


# ---------------- ORDERS ----------------

# Display all orders
def orders_view(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})


# Add an order
def add_order(request):
    if request.method == 'POST':
        customer_id = request.POST['customer']
        total_amount = request.POST['amount']

        customer = get_object_or_404(Customer, id=customer_id)

        Order.objects.create(
            customer=customer,
            total_amount=total_amount
        )

        return redirect('orders')

    

    customers = Customer.objects.all()

    return render(request, 'add_order.html', {'customers': customers})



def orderitems(request):
    if request.method == "POST":
        order_id = request.POST["order"]
        product_id = request.POST["product"]
        quantity = int(request.POST["quantity"])

        order = get_object_or_404(Order, id=order_id)
        product = get_object_or_404(Product, id=product_id)

        price = product.price
        subtotal = price * quantity

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price,
            subtotal=subtotal
        )
        

        return redirect('order_items')

    orders = Order.objects.all()
    products = Product.objects.all()
    orderitems=OrderItem.objects.all()

    return render(
        request,
        'orderitems.html',
        {
            'orders': orders,
            'products': products,
            'orderitems':orderitems
        }
    )
def delete_orderitem(request, id):
    orderitem = get_object_or_404(OrderItem, id=id)
    orderitem.delete()

    return redirect('order_items')

def analytics(request):

    customers = Customer.objects.all()
    total_customer = customers.count()

    sales = OrderItem.objects.all()
    total_sales = sum(item.subtotal for item in sales)

    orders = Order.objects.all()
    total_orders = orders.count()

    products = Product.objects.all()
    total_products = products.count()

    quantity = OrderItem.objects.all()
    total_quantity = sum(item.quantity for item in quantity)

    return render(
        request,
        "analytics.html",
        {
            "total_customers": total_customer,
            "total_price": total_sales,
            "total_orders": total_orders,
            "total_products": total_products,
            "total_quantity": total_quantity
        }
    )
def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()

    return redirect('customers')
def delete_order(request, id):
    customer = get_object_or_404(Order, id=id)
    customer.delete()

    return redirect('orders')
def delete_product(request,id):
    customer=get_object_or_404(Product,id=id)
    customer.delete()

    return redirect('products')