from django.contrib import admin

from . models import Coffee 

# add clasa in pagina admin cu nume,pret si cantitate
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


admin.site.register(Coffee, CoffeeAdmin) 



