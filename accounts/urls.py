from django.urls import path
from .views import signin, signup, profile, logout

app_name = 'accounts'
urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name="logout")
]