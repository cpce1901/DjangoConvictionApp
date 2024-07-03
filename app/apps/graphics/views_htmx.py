import pandas as pd
import pytz
import plotly.express as px
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from apps.sensors.models import Sensor
from apps.lectures.models import Measures
from django.conf import settings
from django.utils import timezone


# Vista para filtrar grupos por Nombre de estudiante
def LoadSensors(request):
    template_name = 'graphics/range_htmx.html'
    locate_id = request.GET.get('locate')
    if locate_id != '':
        sensors = Sensor.objects.get_by_id(locate_id)
        return render(request, template_name, {'sensors': sensors})
    
    sensors = []
    return render(request, template_name, {'sensors': sensors})


def ResultsTopic(request):
    template_name = 'graphics/result_htmx.html'

    vars_mapping = {
    "Va": "Voltaje L1",
    "Vb": "Voltaje L2",
    "Vc": "Voltaje L3",
    "Vab": "Voltaje L1 - L2",
    "Vbc": "Voltaje L2 - L3",
    "Vca": "Voltaje L3 - L1",
    "Ia": "Corriente L1",
    "Ib": "Corriente L2",
    "Ic": "Corriente L3",
    "Pa": "Potencia L1",
    "Pb": "Potencia L2",
    "Pc": "Potencia L3",
    "energy": "Energía",
    "FP": "Factor de Potencia",
    "Hz": "Frecuencia",
    }

    
    topic = request.GET.get('topic')
    sensor = request.GET.get('sensor')
    start_datetime = parse_datetime(request.GET.get('start_datetime'))
    end_datetime = parse_datetime(request.GET.get('end_datetime'))

    measures = Measures.objects.filter_by_sensor_and_date_range_and_topic(
            sensor_code=sensor,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            topic=topic
    )

    local_tz = pytz.timezone(settings.TIME_ZONE)

    sensor = Sensor.objects.get_by_code(sensor)
   
    df = pd.DataFrame(list(measures.values('created', f'{topic}')))
    df['created'] = df['created'].dt.tz_convert(local_tz)

     # Calcular máximo, mínimo y promedio
    maximo = df[topic].max()
    minimo = df[topic].min()
    promedio = df[topic].mean()

    # Redondear los valores a 2 decimales
    maximo = round(maximo, 2)
    minimo = round(minimo, 2)
    promedio = round(promedio, 2)

    if 'V' in topic:
        unit = 'V'
    elif 'I' in topic:
        unit = 'A'
    elif 'P' in topic:
        unit = 'Kw'
    elif 'energy' in topic:
        unit = 'Kw/h'
    elif 'Hz' in topic:
        unit = 'hz'
    else:
        unit = ''
    

    fig = px.line(
        df, 
        x='created', 
        y=f'{topic}',
        title=f'Mediciones de {vars_mapping[topic]} para el sensor {sensor.detail} - {sensor.code}',
        labels={'created': 'Tiempo', f'{topic}': f'{vars_mapping[topic]}'},
        line_shape='linear',  
        render_mode='svg'  
    )
    
    # Personalización para un aspecto más minimalista y colorido
    fig.update_traces(line_color='#FF6B6B', line_width=2)
    chart = fig.to_html()
    
    context = {
        'chart': chart,
        'minimo': round(minimo, 2),
        'maximo': round(maximo, 2),
        'promedio': round(promedio, 2),
        'unit': unit
    }
    return render(request, template_name, context)