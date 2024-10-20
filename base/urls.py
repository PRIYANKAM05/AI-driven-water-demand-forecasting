from django.urls import path
from .views import index, result, HomePage, SignupPage, LoginPage, LogoutPage

urlpatterns = [
    path('', HomePage, name='home'),  # Home page route
    path('index/', index, name='index'),  # Index page
    path('result/', result, name='result'),  # Result page
    path('signup/', SignupPage, name='signup'),  # Signup page
    path('login/', LoginPage, name='login'),  # Login page
    path('logout/', LogoutPage, name='logout'),  # Logout page
]
