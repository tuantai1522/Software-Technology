from app import db
from app.models import Order, OrderDetail
from flask_login import login_user, logout_user, current_user


def count_cart(cart):
    total_quantity = 0
    total_amount = 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity'] * c['price']

    return {
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }


def add_receipt(cart):
    if cart:
        # Add order
        order = Order(user=current_user)
        db.session.add(order)

        # Add Order Details
        for c in cart.values():
            od = OrderDetail(order=order,
                             product_id=c['id'],
                             quantity=c['quantity'],
                             unit_price=c['price'],
                             )
            db.session.add(od)

        db.session.commit()

