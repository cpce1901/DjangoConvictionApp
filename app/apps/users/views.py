from django.views.generic import FormView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import LoginForm


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("graphics_app:home")

    def form_valid(self, form):
        username = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            messages.error(
                self.request,
                "La credenciales ingresadas no son validas. Inténtalo de nuevo.",
            )
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request, *args, **kargs):
        messages.info(self.request, "Haz cerrado la secion exitosamente.")
        logout(request)
        return HttpResponseRedirect(reverse("users_app:login"))


class DetailUser():
    pass


class UpdateUser():
    pass