from typing import Any, Dict
from django.shortcuts import render
#importar los modelos
from vet.models import PetOwner,Pet
from vet.forms import OwnerForm
from django.urls import reverse_lazy
# para importar templates
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView,DetailView,CreateView,UpdateView


def list_pet_owners(request):
    '''List owners'''
    #agarrar info de la DB
    owners=PetOwner.objects.all() 

    # se hace el contecto
    context = {"owners": owners}

    #agarrar template
    template = loader.get_template("vet/owners/list.html")

    return HttpResponse(template.render(context,request))

# class PetList(TemplateView):
#     template_name = "vet/pets/petlist.html" # renderizar el template
#     def get_context_data(self,**kwargs):
#         #toma el contexto de templateview
#         context = super().get_context_data(**kwargs)
#         #agregamos custom context
#         context['pets']= Pet.objects.all()   
#         return context

# class PetDetail(TemplateView):
#     template_name = "vet/pets/petdetails.html"  # Crea un nuevo template para mostrar los detalles

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id = kwargs.get('pk')  # Obtiene el ID de la mascota desde la URL
#         context['pet'] = Pet.objects.get(id=id)# Agrega la mascota al contexto
#         return context

class OwnersCreate(CreateView):
    '''View used to create a PetOwner'''
    # modelo, template y formulario y la url del request si fue exitosa
    model=PetOwner
    template_name= "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

class OwnersUpdate(UpdateView):

    model=PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")




class PetList(ListView):
    '''render a list of pets'''
    model = Pet
    template_name = "vet/pets/petlist.html" # renderizar el template
    context_object_name="pets"

class PetDetail(DetailView):
    '''Renders a specific pet with their pk'''
    #pasar el modelo a manupular
    model = Pet
    #template con el que se va a renderizar
    template_name = "vet/pets/petdetails.html" # renderizar el template
    #contexto
    context_object_name="pet"


class OwnersList(ListView):
    '''render a list of owners'''
    #pasar el modelo a manupular
    model = PetOwner
    #template con el que se va a renderizar
    template_name = "vet/owners/list.html" # renderizar el template
    #contexto
    context_object_name="owners"

class OwnerDetail(DetailView):
    '''Renders a specific owner with their pk'''
    #pasar el modelo a manupular
    model = PetOwner
    #template con el que se va a renderizar
    template_name = "vet/owners/detail.html" # renderizar el template
    #contexto
    context_object_name="owner"

class Test(View):
    
    def get(self,request):
        return HttpResponse('hello word from a class generic view')

