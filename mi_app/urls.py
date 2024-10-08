from django.urls import path
from .views import home, home_admin, login_view, registro

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', registro, name='register'),
    path('home/', home, name='home'),
    path('home_admin/', home_admin, name='home_admin'),
]
