from django.contrib import admin
from pets.models import Pet, Profile

class PetAdmin(admin.ModelAdmin):
    """Class allows you to change default admin interface."""
    pass


admin.site.register(Pet, PetAdmin)
admin.site.register(Profile)
