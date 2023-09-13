
from django.urls import path

from .views import list_pet_owners,Test,OwnersList,OwnerDetail,PetList,PetDetail,OwnersCreate,OwnersUpdate


#poner aliases reverse URL para app  o rutas del proyecto  si no tienes include el alias se escribe como tercer parametro, pero si si tienes include es decir en las url del proyecto el name se agrega como segundo parametro
urlpatterns =[
   path("owners/",OwnersList.as_view(),name='owners_list'),
   path("owners/<int:pk>/",OwnerDetail.as_view(),name="owners_detail"),
   path("owners/add/",OwnersCreate.as_view(),name='owners_create'),
   path("owners/<int:pk>/edit/",OwnersUpdate.as_view(),name='owners_edit'),
   path("pets/",PetList.as_view(),name='pet_list'),
   path("pets/<int:pk>/",PetDetail.as_view(),name='pet_detail'),
   path("test/",Test.as_view()),

]