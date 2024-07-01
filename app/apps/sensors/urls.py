from django.urls import path
from .views import LocatesView
    

app_name = 'sensors_app'

#URLs app CORE
urlpatterns = [
    path('lugares/', LocatesView.as_view(), name='locates'),
    
]