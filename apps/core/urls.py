from django.urls import path
from .views import its_alive, instagram_data

app_name = 'core'

urlpatterns = [
    path('its_alive/', its_alive, name='its_alive'),
    path('instagram_data/', instagram_data, name='its_alive'),
]