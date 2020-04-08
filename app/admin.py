from django.contrib import admin
from .models import ProductsModel,MobilesModel,LaptopsModel,CamerasModel,TelivisionsModel

admin.site.register(ProductsModel)
admin.site.register(MobilesModel)
admin.site.register(LaptopsModel)
admin.site.register(CamerasModel)
admin.site.register(TelivisionsModel)
