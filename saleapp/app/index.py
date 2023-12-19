import hashlib
import math

from flask import render_template, request, redirect, session, jsonify, url_for
from flask_login import login_user, logout_user, login_required

from app import app, login, db

import query
from app.models import User

from app import utils


@app.route('/')
def index():
    categories = query.getAllCategories()

    # get from href or name in "input field"
    cate_id = request.args.get('category_id')
    keyWord = request.args.get('keyWord')
    page = request.args.get("page", 1)

    products = query.loadProducts(cate_id=cate_id, keyWord=keyWord, page=int(page))
    counter = query.countProducts()

    return render_template('index.html',
                           categories=categories,
                           products=products,
                           pages=math.ceil(counter / app.config["PAGE_SIZE"]))


@login.user_loader
def load_user(user_id):
    return query.get_user_by_id(user_id)


@app.route('/log-in')
def log_in_view():
    return render_template('login.html')


@app.route('/admin-login', methods=['post'])
def admin_login():
    error_msg = ""
    if request.method.__eq__('POST'):
        try:
            username = request.form.get('username')
            password = request.form.get('password')

            user = query.checkLogin(username, password)
            if user:
                login_user(user)
                next = request.args.get('next', 'index')
                return redirect(url_for(next))
            else:
                error_msg = "Chuong trinh co loi. Hay kiem tra lai"
        except Exception as ex:
            error_msg = str(ex)

    return render_template('login.html', error_msg=error_msg)


@app.route('/log-out')
def admin_logout():
    logout_user()

    return redirect('/')


@app.route('/sign-up')
def sign_up_view():
    return render_template('signup.html')


@app.route('/admin-signup', methods=['post'])
def admin_signup():
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    avatar = request.form.get('avatar')

    if username and password:
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user = User(name=name, username=username, password=password, avatar=avatar)
        db.session.add(user)
        db.session.commit()

    return redirect('/')


# Cart
# API
@app.route('/api/add-to-cart', methods=['post'])
def addToCart():
    data = request.json

    id = str(data.get('id'))
    name = data.get('name')
    price = data.get('price')

    cart = session.get('cart')

    # chưa tồn tại session nào thì tạo 1 cart mới
    if (not cart):
        cart = {}

    # Sản phẩm đã có trong giỏ
    if (id in cart):
        cart[id]['quantity'] = cart[id]['quantity'] + 1
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


# View
@app.route('/cart', methods=['get', 'post'])
def cart_view():
    cart = session.get('cart')
    total_amount = utils.count_cart(cart)['total_amount']
    total_quantity = utils.count_cart(cart)['total_quantity']

    return render_template('cart.html', cart=cart,
                           total_amount=total_amount,
                           total_quantity=total_quantity)


# Thanh toán
@app.route('/api/pay', methods=['post'])
@login_required
def pay():
    cart = session.get('cart')
    try:
        utils.add_receipt(cart)
        session.clear()
    except:
        return jsonify({'code': 400})

    return jsonify({'code': 200})


# Common
@app.context_processor
def common_response():
    return {
        'categories': query.getAllCategories(),
        'counter_cart': utils.count_cart(session.get('cart'))['total_quantity']
    }


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
