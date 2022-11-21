from django.urls import path
from .views import home, about, coffee

app_name = 'pages'
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('coffee/', coffee, name='coffee'),
]