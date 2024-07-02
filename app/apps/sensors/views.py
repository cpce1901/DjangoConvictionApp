from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Sensor, Located
from urllib.parse import quote
import json


class LocatesView(LoginRequiredMixin, TemplateView):
    template_name = "sensors/locates.html"
    login_url = reverse_lazy("users_app:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        locates = Located.objects.get_by_user(user)
        context['locates'] = locates
        context['enterprise'] = user.enterprise
        return context
    

class SensorsView(LoginRequiredMixin, TemplateView):
    template_name = "sensors/sensors.html"
    login_url = reverse_lazy("users_app:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        slug = self.kwargs["slug"]
        sensors = Sensor.objects.get_by_locate(slug)
        context['slug_locate'] = slug
        context['sensors'] = sensors
        context['enterprise'] = user.enterprise
        return context


class LecturesView(LoginRequiredMixin, TemplateView):
    template_name = "sensors/lectures.html"
    login_url = reverse_lazy("users_app:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        slug_locate = self.kwargs["slug"]
        code_sensor = self.kwargs["code"]
        locate = Located.objects.get_by_slug(slug_locate)
        sensor = Sensor.objects.get_by_code(code_sensor)

        context['topic'] = json.dumps({"topic": str(sensor.topic).replace("/", "-")})
        context['locate'] = locate
        context['sensor'] = sensor.code
        context['enterprise'] = user.enterprise
        return context