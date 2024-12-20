from flask_admin import Admin, BaseView, expose
from app import db, app
from app.models import Category, Product, User, UserRole
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask import redirect

admin = Admin(app=app, name='eCommerce Admin', template_mode='bootstrap4')

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)

class ProductView(AdminView):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['id', 'name', 'price']
    page_size = 10
class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class LogoutView(AuthenticatedView):
    @expose('/')
    def __index__(self):
        logout_user()
        return redirect('/admin')

class StatsView(AuthenticatedView):
    @expose('/')
    def __index__(self):
        return self.render('admin/stats.html')

class CategoryView(AdminView):
    column_list = ['name', 'products']

admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name='Đăng xuất'))