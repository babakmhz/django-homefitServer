from django.contrib import admin
from client.models import (
    serviceCategory,
    bannerSlider,
    subServiceCategory,
    user,
    serviceDate,
    serviceTime,
    availableDateTimeService,order)


# Register your models here.
from django.contrib import admin

admin.site.register(bannerSlider)
admin.site.register(serviceCategory)
admin.site.register(subServiceCategory)
admin.site.register(user)
admin.site.register(serviceDate)
admin.site.register(serviceTime)
admin.site.register(availableDateTimeService)
admin.site.register(order)
# TODO: remove orderd_service from admin mode
# TODO:  make all models read-only
