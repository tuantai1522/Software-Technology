from app import db


def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 1,
        'name': 'Tablet'
    }]


def load_products(kw=None):
    # products = [{
    #     "id": 1,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 2,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 1,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 1,
    #     "name": "iPad Pro 2022",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 1,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }]
    #
    # if kw:
    #     products = [p for p in products if p['name'].find(kw) >= 0]

    products = db.session.get
    return products
