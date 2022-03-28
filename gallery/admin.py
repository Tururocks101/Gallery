from django.contrib import admin
from .models import Images, Categories, Locations

# Register your models here.
admin.site.register(Images)
admin.site.register(Categories)
admin.site.register(Locations)