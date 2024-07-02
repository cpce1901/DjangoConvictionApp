from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Count
from django.conf import settings
from .models import Sensor, Located
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

        context['locate'] = locate
        context['sensor'] = code_sensor
        context['enterprise'] = user.enterprise
        return context