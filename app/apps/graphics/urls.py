from django.urls import path
from .views import HomeView
    

app_name = 'graphics_app'

#URLs app CORE
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
]