from rest_framework.generics import CreateAPIView
from .serializers import LectureSerializer

class CreateLectures(CreateAPIView):
    serializer_class = LectureSerializer