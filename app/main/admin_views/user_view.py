from ..model.user import User

from flask_admin.contrib.sqla import ModelView
from .. import db

class UserView(ModelView):
    can_export = True
    can_create = True
    can_edit = True
    can_delete = True

def create_view(admin):
    admin.add_view(UserView(User, db.session))
