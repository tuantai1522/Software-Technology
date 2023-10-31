from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app import app, db


class Category(db.Model):
    __tablename__ = 'category'
    CategoryID = Column(Integer, primary_key=True, autoincrement=True)
    CategoryName = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    ProductID = Column(Integer, primary_key=True, autoincrement=True)
    ProductName = Column(String(50), nullable=False)
    Price = Column(Float, default=0)
    imageUrl = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.CategoryID), nullable=False)


if __name__ == "__main__":
    from app import app
    with app.app_context():
        # c1 = Category(CategoryName="Mobile")
        # c2 = Category(CategoryName="Tablet")
        #
        p1 = Product(ProductName = "Iphone 14", Price = "10000000", category_id = 1)
        p2 = Product(ProductName = "Iphone 14 Plus", Price = "12000000", category_id = 1)
        p3 = Product(ProductName = "Iphone 15", Price = "18000000", category_id = 1)
        p4 = Product(ProductName = "Iphone 14 Pro", Price = "14000000", category_id = 1)
        p5 = Product(ProductName = "Iphone 14 Pro Max", Price = "16000000", category_id = 1)
        p6 = Product(ProductName = "Iphone 15 Plus", Price = "20250000", category_id = 1)

        db.session.add_all({p1, p2, p3, p4, p5, p6})
        db.session.commit()
        # db.create_all()