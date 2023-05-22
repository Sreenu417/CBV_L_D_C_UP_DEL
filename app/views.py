from django.shortcuts import render

# Create your views here.
from app.models import *

from django.views.generic import TemplateView,ListView,DetailView,CreateView


class home(TemplateView):
    template_name='app/Home.html'



# This class based view is used for Displaying The List of objects Data           It is under ListView

class SchoolList(ListView):
    model=School
    context_object_name='schools'


#This class based view is used for Displaying Details of selected objects        It is under DetailView

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'


# This class based view is used for Creating or  Inserting the Data           It is under CreateView


class SchoolCreate(CreateView):
    model=School
    fields='__all__'
