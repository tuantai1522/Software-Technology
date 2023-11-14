from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user

from flask import render_template, request, redirect

from app.models import Product, Category, User, UserRole
from app import app, db

class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.Admin

class MyProductView(AuthenticatedModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_filters = ['price', 'name']
    column_editable_list = ['name', 'price']
    details_modal = True
    edit_modal = True

class MyCategoryView(AuthenticatedModelView):
    column_list = ['name', 'products']


class AuthenticatedBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class StaticView(AuthenticatedBaseView):
    @expose('/')
    def index(self):
        return self.render('admin/static-view.html')

class LogoutView(AuthenticatedBaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

class SignupView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/signup.html')

    def is_accessible(self):
        return not current_user.is_authenticated


admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))

# In this view => I don't create MyUserView
admin.add_view(AuthenticatedModelView(User, db.session))

admin.add_view(StaticView(name="Thống kê báo cáo"))
admin.add_view(SignupView(name="Đăng ký"))
admin.add_view(LogoutView(name="Đăng xuất"))
