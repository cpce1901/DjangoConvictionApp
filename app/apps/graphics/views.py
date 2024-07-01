from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'graphics/home.html'
    login_url = reverse_lazy("users_app:login")