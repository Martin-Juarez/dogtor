from django.shortcuts import render
from rest_framework import viewsets,generics
from vet.models import PetOwner, Pet
from .serializers import OwnersSerializers,PetSerializer,OwnersListSerializer,OwnerSerializer
# Create your views here.

#class OwnersViewSet(viewsets.ModelViewSet):
#    '''view set to model pet'''

# 1. queryset que se va realizar 
#    queryset = PetOwner.objects.all()

# 2. El serializador
#    serializer_class =  OwnersSerializers

#class PetsViewSet(viewsets.ModelViewSet):

#    queryset = Pet.objects.all()
#    serializer_class = PetSerializer

class ListOwnersAPIView(generics.ListAPIView):
    '''List owners Api view'''

    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    '''List owners Api view'''

    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnerSerializer

##############################################################
class CreateOwnerAPIView(generics.CreateAPIView):
    '''Create owner Api view'''

    quertyset = PetOwner.objects.create() 
    serializer_class = OwnerSerializer


class UpdateOwnerAPIView(generics.UpdateAPIView):
     '''Update Api view'''

     queryset = PetOwner.objects.all()
     serializer_class = OwnerSerializer


class DeleteOwnerAPIView(generics.DestroyAPIView):
     '''List owners Api view'''

     queryset = PetOwner.objects.all()
     serializer_class = OwnerSerializer

