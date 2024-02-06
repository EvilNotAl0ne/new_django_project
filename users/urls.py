from django.urls import path
from .views import log_out, register, log_in, get_user_info

app_name = "users"
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", log_in, name="login"),
    path("logout/", log_out, name="logout"),
    path("user/<int:pk>/", get_user_info, name="user_info"),
] 
