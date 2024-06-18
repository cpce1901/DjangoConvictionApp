from django.urls import path
from .views import llama_view

urlpatterns = [
    path('', llama_view),
]