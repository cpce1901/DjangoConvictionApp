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
        return context
    
   