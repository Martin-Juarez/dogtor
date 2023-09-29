from django.contrib import admin
from . import models

# Register your models here.


#panel de administracion para el area de blog
class VetAdminArea(admin.AdminSite):
    '''Blog admin Area panel de administracion'''

    site_header = "Pet Admin Panel"

#instanciar nuestra clase

vet_admin_site = VetAdminArea(name="VetAdmin")

vet_admin_site.register(models.PetOwner)
vet_admin_site.register(models.Pet)
vet_admin_site.register(models.PetDate)


#registrarlo en el admin principal
admin.site.register(models.PetOwner)
admin.site.register(models.Pet)
admin.site.register(models.PetDate)