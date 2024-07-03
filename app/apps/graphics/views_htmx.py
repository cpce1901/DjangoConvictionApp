import pandas as pd
import plotly.express as px
from django.shortcuts import render
from apps.sensors.models import Sensor


# Vista para filtrar grupos por Nombre de estudiante
def LoadSensors(request):
    template_name = 'graphics/range_htmx.html'
    locate_id = request.GET.get('locate')
    if locate_id != '':
        sensors = Sensor.objects.get_by_id(locate_id)
        return render(request, template_name, {'sensors': sensors})
    
    sensors = []
    return render(request, template_name, {'sensors': sensors})