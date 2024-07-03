from datetime import datetime
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.utils.dateparse import parse_datetime
from .forms import RangeSensorsForm
from apps.lectures.models import Measures


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'graphics/home.html'
    login_url = reverse_lazy("users_app:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['enterprise'] = user.enterprise
        return context
    

class RangeGraphicView(LoginRequiredMixin, FormView):
    template_name = 'graphics/range.html'
    login_url = reverse_lazy("users_app:login")
    form_class = RangeSensorsForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        locate = cleaned_data['locate']
        sensor = cleaned_data['sensors']
        
        # Combinar fecha y hora para crear objetos datetime
        date_time_1 = datetime.combine(cleaned_data['date_1'], cleaned_data['time_1'])
        date_time_2 = datetime.combine(cleaned_data['date_2'], cleaned_data['time_2'])

        # Convertir a la zona horaria de Django si es necesario
        date_time_1 = timezone.make_aware(date_time_1)
        date_time_2 = timezone.make_aware(date_time_2)

        # Crear la URL con los parámetros
        url = reverse('graphics_app:range-resume')
        url += f'?locate={locate}&sensor={sensor}'
        url += f'&start_datetime={date_time_1.isoformat()}'
        url += f'&end_datetime={date_time_2.isoformat()}'

        return HttpResponseRedirect(url)
    

class RangeGraphicResumeView(LoginRequiredMixin, TemplateView):
    template_name = 'graphics/range_result.html'
    login_url = reverse_lazy("users_app:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        locate = self.request.GET.get('locate')
        sensor = self.request.GET.get('sensor')
        start_datetime = parse_datetime(self.request.GET.get('start_datetime'))
        end_datetime = parse_datetime(self.request.GET.get('end_datetime'))

        measures = Measures.objects.filter_by_sensor_and_date_range(
            sensor_code=sensor,
            start_datetime=start_datetime,
            end_datetime=end_datetime
        )

        context['results'] = measures

        return context
    