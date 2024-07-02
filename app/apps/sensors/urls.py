from django.urls import path
from .views import LocatesView, SensorsView, LecturesView
    

app_name = 'sensors_app'

#URLs app CORE
urlpatterns = [
    path('lugares/', LocatesView.as_view(), name='locates'),
    path('lugares/<slug:slug>/', SensorsView.as_view(), name='sensors'),
    path('lugares/<slug:slug>/<str:code>/', LecturesView.as_view(), name='lectures'),
    
]