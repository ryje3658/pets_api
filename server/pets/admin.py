from django.contrib import admin
from pets.models import Pet

class PetAdmin(admin.ModelAdmin):
    """Class allows you to change default admin interface."""
    pass


admin.site.register(Pet, PetAdmin)
