import hashlib
import math

from flask import render_template, request, redirect
from flask_login import login_user

from app import app, login, db

import query
from app.models import User


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
                           pages = math.ceil(counter / app.config["PAGE_SIZE"]))

@login.user_loader
def load_user(user_id):
    return query.get_user_by_id(user_id)

@app.route('/admin-login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = query.checkLogin(username, password)
    if user:
        login_user(user)

    return redirect('/admin')

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

    return redirect('/admin')

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)



