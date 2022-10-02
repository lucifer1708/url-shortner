from django.urls import path
from .views import home, redirecturl

app_name = 'url'

urlpatterns = [
    path('', home, name='home'),
    path('<str:pk>', redirecturl, name='redirecturl')
]
