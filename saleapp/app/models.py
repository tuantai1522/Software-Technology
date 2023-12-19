from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime, Boolean
from sqlalchemy.orm import relationship
from app import db, app

from flask_login import UserMixin
from enum import Enum as UserEnum


class UserRole(UserEnum):
    Admin = 1,
    User = 2


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    joined_date = Column(DateTime, default=datetime.now())
    avatar = Column(String(100))
    user_role = Column(Enum(UserRole), default=UserRole.User)

    # Order
    orders = relationship("Order", backref="user", lazy=True)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))

    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    order_details = relationship("OrderDetail", backref="product", lazy=True)


    def __str__(self):
        return self.name


class Order(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    order_details = relationship("OrderDetail", backref="order", lazy=True)


class OrderDetail(db.Model):
    order_id = Column(Integer, ForeignKey(Order.id), nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False, primary_key=True)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        #
        # import hashlib
        #
        # u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        # db.session.add(u)
        #
        # p1 = Product(name='iPhone 13', price=20000000, category_id=1,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p2 = Product(name='Galaxy S23 Plus', price=22000000, category_id=1,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p3 = Product(name='iPad Pro 2023', price=35000000, category_id=2,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p4 = Product(name='Galaxy Tab S9', price=24000000, category_id=2,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # p5 = Product(name='Note 23', price=20000000, category_id=1,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
