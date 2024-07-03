from django.urls import path
from .viewsets import CreateLectures

app_name = 'lectures_app'

urlpatterns = [
    path('lectures/add/', CreateLectures.as_view(), name='lecture-add'),
  
]