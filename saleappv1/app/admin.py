from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from app import app, db
from app.models import Category, Product

from flask_admin import BaseView, expose


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price']
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    column_editable_list = ['name']

class MyCategoryView(ModelView):
    column_list = ['id', 'name', 'products']

class StasView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin = Admin(app=app, name="Quản trị bán hàng", template_mode='bootstrap4')
admin.add_view(MyCategoryView(Category, db.session))

admin.add_view(MyProductView(Product, db.session))
admin.add_view(StasView(name="Thống kê báo cáo"))
