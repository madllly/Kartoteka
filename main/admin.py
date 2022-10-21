from django.contrib import admin
from .models import *


class estate_admin(admin.ModelAdmin):
    list_display = ('count_room', 'floor', 'square_meters', 'region')

class region_admin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(estate, estate_admin)
admin.site.register(region,region_admin)
