from django.contrib import admin
from .models import OwnerShipType, NumberChoices, Country, Region, DemandType, DemandCategory, Source

admin.site.register(OwnerShipType)
admin.site.register(NumberChoices)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(DemandCategory)
admin.site.register(DemandType)
admin.site.register(Source)
