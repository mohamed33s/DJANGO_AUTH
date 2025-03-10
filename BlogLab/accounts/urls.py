from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("add_post_perm/", views.add_post_permission, name="add_post_perm"),
    path("add_to_group_editors/", views.add_to_group_editors, name="add_to_group_editors"),
]