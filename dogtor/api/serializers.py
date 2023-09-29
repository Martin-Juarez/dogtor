from rest_framework import serializers
from vet.models import  PetOwner,Pet

class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    '''Pet owner serializer'''
# los serializadores son la reprsentacion de la API
    class Meta:
        model = PetOwner
        fields = ['id','first_name','last_name','email','address','phone','created_at']


class PetSerializer(serializers.HyperlinkedModelSerializer):
    '''Pet list serializer'''
# los serializadores son la reprsentacion de la API

    owner = serializers.PrimaryKeyRelatedField(queryset=PetOwner.objects.all(),many=False)
    class Meta:
        model = Pet
        fields = ['id','name','type','created_at','owner']




class OwnersListSerializer(serializers.ModelSerializer):
    '''serializer to list pet owner'''
    class Meta:
        model = PetOwner
        fields = ['id','first_name','last_name']

class OwnerSerializer(serializers.ModelSerializer):
    '''serializer to list pet owner'''
    class Meta:
        model = PetOwner
        fields = "__all__"

# class CreateOwnerSerializer(serializers.ModelSerializer):
#     '''serializer to list pet owner'''
#     class Meta:
#         model = PetOwner
#         fields = "__all__"

