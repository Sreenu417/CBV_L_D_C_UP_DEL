from django.shortcuts import render

# Create your views here.
from app.models import *

from django.views.generic import TemplateView,ListView


class home(TemplateView):
    template_name='app/Home.html'



class SchoolList(ListView):
    model=School
    context_object_name='schools'