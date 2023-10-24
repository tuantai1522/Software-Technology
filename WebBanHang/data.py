def load_categories():
    return [{
        "id": 1,
        "name": "Iphone"
    }, {
        "id": 2,
        "name": "Ipad"
    }, {
        "id": 3,
        "name": "Apple watch"
    }]


def load_products(keyWord):
    products = [{
        "id": 1,
        "name": "Iphone 15",
        "price": 18000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    }, {
        "id": 2,
        "name": "Iphone 15 Plus",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"

    }, {
        "id": 3,
        "name": "Iphone 15 Pro",
        "price": 22000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"

    }, {
        "id": 4,
        "name": "Iphone 15 Pro Max",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    }, {
        "id": 5,
        "name": "Iphone 14",
        "price": 10000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    }, {
        "id": 6,
        "name": "Iphone 14 Plus",
        "price": 12000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    }, {
        "id": 7,
        "name": "Iphone 14 Pro",
        "price": 10000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },
    ]
    if keyWord:
        products = [p for p in products if p['name'].find(keyWord) >= 0]

    return products

