from rest_framework import serializers
from .models import Measures
from apps.sensors.models import Sensor

class LectureSerializer(serializers.ModelSerializer):
    # Campo para recibir el código del sensor
    sen = serializers.CharField(write_only=True)

    class Meta:
        model = Measures
        fields = ['sen', 'Va', 'Vb', 'Vc', 'Vca', 'Vab', 'Vbc', 'Ia', 'Ib', 'Ic', 'Pa', 'Pb', 'Pc', 'FP', 'Hz']
        # No incluimos 'energy' ni 'sensor' aquí porque los manejaremos manualmente

    def validate(self, data):       
        # Obtener el sensor basado en el código
        try:
            code = str(data['sen']).replace('-', '/')
            topic = f'{code}/'
            sensor = Sensor.objects.get(topic=topic)
            data['sensor'] = sensor
        except Sensor.DoesNotExist:
            raise serializers.ValidationError("No se encontró un sensor con el código proporcionado.")

        # Eliminar sensor_code del diccionario data ya que no es un campo del modelo
        del data['sen']

        # Calcular energy
        data['energy'] = data['Pa'] + data['Pb'] + data['Pc']

        data['Va'] = data['Va'] * 0.01
        data['Vb'] = data['Vb'] * 0.01
        data['Vc'] = data['Vc'] * 0.01

        data['Vca'] = data['Vca'] * 0.01
        data['Vab'] = data['Vab'] * 0.01
        data['Vbc'] = data['Vbc'] * 0.01

        data['FP'] = round((data['FP'] * 0.001), 2)
        data['Hz'] = round((data['Hz'] * 0.01), 2)

        return data

    def create(self, validated_data):
        return Measures.objects.create(**validated_data)

    