from django.urls import path, include
from .views import LoginView, home, SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("register", SignUpView.as_view(), name="register"),
]