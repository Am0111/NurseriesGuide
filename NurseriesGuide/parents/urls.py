from django.urls import path
from . import views

app_name = "parents"

urlpatterns = [

    path('logout/', views.log_out, name="log_out"),
    path('add/', views.add_child, name="add_child"),
    path('delete/child/<int:child_id>', views.delete_child, name="delete_child"),
    path('update/child/<int:child_id>', views.update_child, name="update_child"),
    path('update/user/', views.update_user, name="update_user"),
    path('requests-status/', views.requests_status, name="requests_status"),
    path('signup/manager/', views.signup_manager, name="signup_manager"),
    path('signup/parent/', views.signup_parent, name="signup_parent"),
    path('signin/', views.signin, name="signin"),
    path('profile/', views.parent_profile, name="parent_profile"),



]


