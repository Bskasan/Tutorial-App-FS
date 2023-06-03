from django.shortcuts import render
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class TutorialView(ModelViewSet):
    pass
