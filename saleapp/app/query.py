import hashlib

from app import app, login
from app.models import Category, Product, User

def getAllCategories():
    return Category.query.all()


def loadProducts(cate_id=None, keyWord=None, page=1):
    page_size = app.config["PAGE_SIZE"]
    start = (page - 1) * page_size
    end = start + page_size

    if cate_id:
        return Product.query.filter(Product.category_id.__eq__(cate_id)).slice(start, end)

    if keyWord:
        return Product.query.filter(Product.name.contains(keyWord)).slice(start, end)

    return Product.query.slice(start, end).all()

def countProducts():
    return Product.query.filter().count()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def checkLogin(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()