from django.urls import path
from .views import HomeView, RangeGraphicView, RangeGraphicResumeView
from .views_htmx import LoadSensors, ResultsTopic
    
app_name = 'graphics_app'

url_app = [
    path('', HomeView.as_view(), name='home'),
    path('graficos/', RangeGraphicView.as_view(), name='range'),
    path('graficos/resumen/', RangeGraphicResumeView.as_view(), name='range-resume'),
]

url_htmx = [
    path('graficos/graficos-filtro/', LoadSensors, name='range-htmx'),
    path('graficos/resumen/graficos-results/', ResultsTopic, name='topic-result-htmx'),
]

urlpatterns =  url_htmx + url_app