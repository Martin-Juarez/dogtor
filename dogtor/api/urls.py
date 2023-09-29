from django.urls import path,include
from .views import ListOwnersAPIView,RetrieveOwnersAPIView,CreateOwnerAPIView,UpdateOwnerAPIView,DeleteOwnerAPIView
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r"owners",OwnersViewSet) 
# registramos los endpoint "owners/->GET","owners/POST", DELETE
#router.register(r"pet",PetsViewSet) 

urlpatterns = [
#    path("",include(router.urls))
     path('owners/',ListOwnersAPIView.as_view(),name="owner_list"),
     path('owners/<int:pk>/',RetrieveOwnersAPIView.as_view(),name='owners_detail'),
     path('owners/add/',CreateOwnerAPIView.as_view(),name='create_owner'),
     path('update/<int:pk>/',UpdateOwnerAPIView.as_view(), name='update_owner'),
     path('delete/<int:pk>/',DeleteOwnerAPIView.as_view(), name='delete_owner'),
]