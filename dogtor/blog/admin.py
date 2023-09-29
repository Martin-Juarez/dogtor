from django.contrib import admin
from . import models





#decorator

@admin.register(models.Post)

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    '''Post admin model for admin'''
    fields = ["name"]





#panel de administracion para el area de blog
class BlogAdminArea(admin.AdminSite):
    '''Blog admin Area panel de administracion'''

    site_header = "Blog Admin Panel"

#instanciar nuestra clase

Blog_Admin_site = BlogAdminArea(name="BlogAdmin")

Blog_Admin_site.register(models.Post,PostAdmin)

#registrarlo en el admin principal
#admin.site.register(models.Post,PostAdmin)