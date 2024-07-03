from datetime import datetime, timedelta
from django import forms
from apps.sensors.models import Located, Sensor
from apps.lectures.models import Measures

class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
    

class RangeSensorsForm(forms.Form):
    locate = NameModelChoiceField(
        label='Lugares de instalación',
        queryset=Located.objects.none(),
        required=True,
        widget=forms.Select(
            attrs={
                "hx-get": "graficos-filtro/",
                "hx-trigger": "change",
                "hx-target": "#id_sensors",
                "class": "w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200",
            }
        )
    )

    sensors = forms.ModelChoiceField(
        queryset=Sensor.objects.none(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200",
            }
        )
    )

    date_1 = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "class": "w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200",
                "type": "date"
            }
        )
    )

    date_2 = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "class": "w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200",
                "type": "date"
            }
        )
    )

    time_1 = forms.TimeField(
        required=True,
        widget=forms.TimeInput(
            attrs={
                "class": "w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200",
                "type": "time"
            }
        )
    )

    time_2 = forms.TimeField(
        required=True,
        widget=forms.TimeInput(
            attrs={
                "class": "w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 transition duration-200",
                "type": "time"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['locate'].queryset = Located.objects.get_by_user(user)
        
        if 'locate' in self.data:
            try:
                locate_id = int(self.data.get('locate'))
                self.fields["sensors"].queryset = Sensor.objects.get_by_id(locate_id)
            except (ValueError, TypeError):
                pass

        # Establecer horas iniciales (opcional)
        self.fields['time_1'].initial = datetime.now().replace(hour=0, minute=0, second=0).time()
        self.fields['time_2'].initial = datetime.now().time()




