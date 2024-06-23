"""from django.contrib import admin
from .models import Data, Regions

class RegionsInline(admin.TabularInline):
    model = Regions
    extra = 1

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('country', 'population', 'latitude', 'longitude')
    inlines = [RegionsInline]

@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'data')
    list_filter = ('data',)
    search_fields = ('name',)"""""



##test 2 avec l'ajout de la classe ecoles
from django.contrib import admin
from .models import Data, Regions, Ecoles

class RegionsInline(admin.TabularInline):
    model = Regions
    extra = 1

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('country', 'population', 'latitude', 'longitude')
    inlines = [RegionsInline]

@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'data')
    list_filter = ('data',)
    search_fields = ('name',)

@admin.register(Ecoles)
class EcolesAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'long')
    search_fields = ('name',)
