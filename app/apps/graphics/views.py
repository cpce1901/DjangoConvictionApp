from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'graphics/home.html'
    login_url = reverse_lazy("users_app:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['enterprise'] = user.enterprise
        return context